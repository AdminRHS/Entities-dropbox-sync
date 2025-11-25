"""
Priority Score Calculator for Video Queue System
Calculates 0-100 priority score based on video metadata
"""

from datetime import datetime, timedelta


def calculate_priority_score(video_metadata):
    """
    Calculate priority score 0-100 based on:
    - Views (30% weight) - normalized to 0-30
    - Likes (20% weight) - normalized to 0-20
    - Recency (30% weight) - newer = higher score
    - Engagement rate (20% weight) - likes/views ratio

    Args:
        video_metadata (dict): Dictionary containing video metadata with keys:
            - 'views' (int): Video view count
            - 'likes' (int): Video like count
            - 'publish_date' (str or datetime): Publication date (YYYY-MM-DD format)

    Returns:
        float: Priority score from 0-100 (rounded to 2 decimal places)
    """

    # Extract metadata
    views = int(video_metadata.get('views', 0))
    likes = int(video_metadata.get('likes', 0))
    publish_date = video_metadata.get('publish_date', datetime.now())

    # Convert publish_date to datetime if it's a string
    if isinstance(publish_date, str):
        try:
            publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
        except ValueError:
            # If parsing fails, assume recent date
            publish_date = datetime.now()

    # Calculate views score (30% weight)
    # 1M views = max 30 points
    views_score = min(30, (views / 1000000) * 30)

    # Calculate likes score (20% weight)
    # 50K likes = max 20 points
    likes_score = min(20, (likes / 50000) * 20)

    # Calculate recency score (30% weight)
    # 30 points for brand new, linearly decreasing to 0 after 365 days
    days_since_publish = (datetime.now() - publish_date).days
    recency_score = max(0, 30 - (days_since_publish / 365) * 30)

    # Calculate engagement score (20% weight)
    # Engagement rate = likes/views ratio
    # 1% engagement = 20 points
    if views > 0:
        engagement_rate = likes / views
        engagement_score = min(20, engagement_rate * 2000)  # 1% = 20 points
    else:
        engagement_score = 0

    # Total score
    total_score = views_score + likes_score + recency_score + engagement_score

    return round(total_score, 2)


def calculate_priority_with_details(video_metadata):
    """
    Calculate priority score and return detailed breakdown.

    Args:
        video_metadata (dict): Dictionary containing video metadata

    Returns:
        dict: Priority score and component breakdown
    """

    views = int(video_metadata.get('views', 0))
    likes = int(video_metadata.get('likes', 0))
    publish_date = video_metadata.get('publish_date', datetime.now())

    if isinstance(publish_date, str):
        try:
            publish_date = datetime.strptime(publish_date, '%Y-% m-%d')
        except ValueError:
            publish_date = datetime.now()

    views_score = min(30, (views / 1000000) * 30)
    likes_score = min(20, (likes / 50000) * 20)

    days_since_publish = (datetime.now() - publish_date).days
    recency_score = max(0, 30 - (days_since_publish / 365) * 30)

    if views > 0:
        engagement_rate = likes / views
        engagement_score = min(20, engagement_rate * 2000)
    else:
        engagement_rate = 0
        engagement_score = 0

    total_score = views_score + likes_score + recency_score + engagement_score

    return {
        'total_score': round(total_score, 2),
        'views_score': round(views_score, 2),
        'likes_score': round(likes_score, 2),
        'recency_score': round(recency_score, 2),
        'engagement_score': round(engagement_score, 2),
        'views': views,
        'likes': likes,
        'engagement_rate': round(engagement_rate * 100, 2) if engagement_rate else 0,  # as percentage
        'days_since_publish': days_since_publish
    }


# CLI interface for testing
if __name__ == '__main__':
    import sys

    # Test with sample data if no arguments
    if len(sys.argv) < 4:
        print("Usage: python calculate_priority.py <views> <likes> <publish_date>")
        print("\nExample: python calculate_priority.py 1500000 45000 2025-10-15")
        print("\nTesting with sample data...")

        # Sample test cases
        test_cases = [
            {
                'name': 'High-performing recent video',
                'views': 1500000,
                'likes': 45000,
                'publish_date': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            },
            {
                'name': 'Viral video with high engagement',
                'views': 5000000,
                'likes': 200000,
                'publish_date': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            },
            {
                'name': 'Older video with moderate views',
                'views': 500000,
                'likes': 15000,
                'publish_date': (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')
            },
            {
                'name': 'Low-performing video',
                'views': 10000,
                'likes': 200,
                'publish_date': (datetime.now() - timedelta(days=60)).strftime('%Y-%m-%d')
            }
        ]

        for test in test_cases:
            print(f"\n{'='*60}")
            print(f"Test: {test['name']}")
            print(f"{'='*60}")
            details = calculate_priority_with_details(test)
            print(f"Views: {details['views']:,}")
            print(f"Likes: {details['likes']:,}")
            print(f"Days since publish: {details['days_since_publish']}")
            print(f"Engagement rate: {details['engagement_rate']}%")
            print(f"\nScore Breakdown:")
            print(f"  Views score (30% max):      {details['views_score']:.2f}")
            print(f"  Likes score (20% max):      {details['likes_score']:.2f}")
            print(f"  Recency score (30% max):    {details['recency_score']:.2f}")
            print(f"  Engagement score (20% max): {details['engagement_score']:.2f}")
            print(f"  {'─'*40}")
            print(f"  TOTAL PRIORITY SCORE:       {details['total_score']:.2f}/100")
    else:
        # Calculate from command-line arguments
        views = int(sys.argv[1])
        likes = int(sys.argv[2])
        publish_date = sys.argv[3]

        metadata = {
            'views': views,
            'likes': likes,
            'publish_date': publish_date
        }

        details = calculate_priority_with_details(metadata)
        print(f"\nPriority Score: {details['total_score']}/100")
        print(f"\nBreakdown:")
        print(f"  Views: {details['views_score']:.2f}/30")
        print(f"  Likes: {details['likes_score']:.2f}/20")
        print(f"  Recency: {details['recency_score']:.2f}/30")
        print(f"  Engagement: {details['engagement_score']:.2f}/20")
