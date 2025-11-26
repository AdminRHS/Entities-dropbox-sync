# Video Generation - AI Tools Prompt

**Purpose:** Comprehensive guide for selecting and using AI video generation tools based on project requirements  
**Version:** 1.0  
**Date:** 2025-01-27  
**Status:** Active  
**Category:** AI Tools - Video Generation  
**Related Tools:** Sora, Kling, RunwayML, Synthesia, HeyGen, Seedream, VAYU, Hedra

---

## Overview

This prompt helps you select the appropriate AI video generation tool based on your specific project requirements, content type, and workflow needs. The video generation ecosystem includes tools for text-to-video, image-to-video, AI avatars, video editing, and specialized effects.

---

## Tool Selection Matrix

### 1. Text-to-Video Generation

**When to Use:** Creating videos from text descriptions or prompts

#### **Sora (OpenAI) - TOOL-AI-047**
**Best For:**
- High-quality, cinematic video generation
- Complex scenes with multiple characters
- Professional marketing and commercial content
- Educational and explainer videos
- Up to 60-second videos at 1080p resolution

**Key Strengths:**
- State-of-the-art video quality
- Excellent temporal consistency
- Realistic physics and motion
- Multiple aspect ratios (16:9, 9:16, 1:1)
- Cinematic camera movements
- Integration with OpenAI ecosystem

**Limitations:**
- Subscription required (ChatGPT Plus/Pro)
- Limited availability (gradual rollout)
- Video length up to 60 seconds
- Generation time can be slow
- Content policy restrictions

**Cost:** Subscription-based (OpenAI pricing, typically bundled with ChatGPT Plus/Pro)

**Integration:**
- GLIF for workflow automation
- Premiere Pro, After Effects for post-production
- Eleven Labs for voiceovers
- Midjourney/Stable Diffusion for reference images

**Prompt Engineering Tips:**
- Be specific about camera angles and movements
- Describe lighting and mood in detail
- Specify character actions and interactions clearly
- Include time of day and environmental details
- Mention desired style (cinematic, documentary, etc.)

---

#### **Kling (Kuaishou Technology) - TOOL-AI-048**
**Best For:**
- Short-form social media content (5-10 seconds)
- Fast video generation
- Social media marketing videos
- Product videos with motion
- B-roll footage generation

**Key Strengths:**
- Excellent motion quality and realism
- Fast generation speed
- Strong temporal consistency
- Competitive pricing with free tier
- Multiple aspect ratio support
- Effective for social media content

**Limitations:**
- Video length limitations (5-10 seconds per generation)
- May struggle with very complex multi-character scenes
- Free tier has credit limitations
- Generation queue wait times during peak usage

**Cost:** Freemium (Free credits available + paid plans)

**Integration:**
- GLIF for workflow automation
- CapCut for video editing
- Social media platforms for direct publishing
- Eleven Labs for voiceover integration

**Prompt Tips:**
- Be specific about camera angle and movement
- Describe motion clearly (speed, direction)
- Include lighting and atmosphere details
- Keep prompts focused on single clear action
- Use descriptive adjectives for mood

---

### 2. Image-to-Video Conversion

**When to Use:** Animating static images or creating videos from reference images

**Tools:**
- **Sora** - High-quality image-to-video with temporal consistency
- **Kling** - Fast image-to-video for social media
- **RunwayML** - Professional image-to-video with editing capabilities

**Workflow:**
1. Generate or select reference image (Midjourney, Stable Diffusion, etc.)
2. Upload image to video generation tool
3. Describe desired motion and camera movement
4. Set video duration and style parameters
5. Generate and review
6. Post-process if needed

---

### 3. AI Avatar Video Generation

**When to Use:** Creating videos with AI avatars for training, marketing, or corporate communications

#### **Synthesia - TOOL-AI-050**
**Best For:**
- Enterprise-grade professional videos
- Training and educational content
- Multilingual video production
- Corporate communications
- Template-based video creation

**Key Strengths:**
- Professional quality output
- Large avatar library
- Multilingual support (140+ languages)
- Template library
- Team collaboration features
- Enterprise features

**Limitations:**
- Higher cost (from $22/month per user)
- Limited customization in lower tiers
- Processing time required
- Subscription required for full features

**Cost:** Subscription-based (Plans from $22/month per user)

**Use Cases:**
- Create training videos
- Produce marketing videos
- Draft corporate communications
- Produce multilingual videos
- Create personalized videos
- Create educational content

---

#### **HeyGen - TOOL-AI-048**
**Best For:**
- AI video generation with realistic avatars
- Voice cloning integration
- Multilingual video creation
- Marketing and promotional videos
- Personalized video content

**Key Strengths:**
- Realistic AI avatars
- Voice cloning technology
- Multilingual support
- Easy to use interface
- Professional quality output
- No actors needed

**Limitations:**
- Subscription required for full features
- Limited avatar customization in free tier
- Processing time for videos
- May require refinement

**Cost:** Freemium (Free tier available, paid plans from $24/month)

**Use Cases:**
- Create video avatars
- Produce multilingual videos
- Clone voices for videos
- Produce marketing videos
- Produce training videos
- Create personalized videos

---

### 4. Video Editing and Effects

**When to Use:** Editing, enhancing, or adding effects to existing or generated videos

#### **RunwayML - TOOL-AI-039**
**Best For:**
- Professional video editing
- AI-powered video effects
- Image-to-video conversion
- Video manipulation and enhancement
- Creative video production

**Key Strengths:**
- Professional video editing capabilities
- AI-powered effects and generation
- Multiple video editing tools
- Image-to-video conversion
- High-quality output

**Limitations:**
- Subscription required for full features
- Learning curve for advanced features
- Processing time for complex videos

**Cost:** Subscription-based (Free tier available, paid plans from $12/month)

**Use Cases:**
- Generate video content
- Edit videos
- Convert images to video
- Produce creative videos
- Create marketing videos

---

### 5. Specialized Video Effects

**When to Use:** Creating unique visual styles or specialized effects

#### **Seedream - TOOL-AI-050**
**Best For:**
- Tilt-shift and miniature-style videos
- Documentary-style content
- Creative visual effects
- Short-form social media content (30-60 seconds)
- Historical and location showcases

**Key Strengths:**
- Distinctive tilt-shift/miniature aesthetic
- Creates engaging, eye-catching content
- Excellent for social media engagement
- Pairs seamlessly with VAYU 2.2
- Automated workflow integration via GLIF
- Effective for short-form content

**Limitations:**
- Specialized aesthetic (not suitable for all content types)
- Best used in combination with other tools (VAYU)
- Primarily accessed via GLIF workflows
- Optimized for specific video lengths (30-60 seconds)

**Cost:** Usage-based (typically accessed via GLIF workflows)

**Best Practices:**
- Combine with VAYU 2.2 for optimal tilt-shift effects
- Use GLIF workflows for efficient automation
- Keep videos 30-60 seconds for social media engagement
- Choose elevated camera angles for best miniature effect
- Add professional voiceover for documentary content

**Workflow Integration:**
- GLIF - Workflow automation and orchestration
- VAYU 2.2 - Combined for enhanced miniature effects
- Eleven Labs - Professional voiceover narration
- Perplexity - Content research for documentaries

---

#### **VAYU - TOOL-AI-XXX**
**Best For:**
- Video effects enhancement
- Combining with other video generation tools
- Specialized visual effects

**Integration:**
- Pairs with Seedream for enhanced miniature effects
- Used in automated GLIF workflows

---

## Decision Framework

### Step 1: Identify Your Content Type

**Marketing/Commercial Content:**
- **Primary:** Sora (for quality) or Kling (for speed)
- **Alternative:** Synthesia or HeyGen (for avatar-based content)
- **Post-production:** RunwayML

**Social Media Content:**
- **Primary:** Kling (fast, short-form optimized)
- **Creative:** Seedream + VAYU (unique aesthetic)
- **Avatar-based:** HeyGen

**Training/Educational Content:**
- **Primary:** Synthesia (enterprise features, templates)
- **Alternative:** Sora (for explainer videos)
- **Creative:** Seedream (for engaging educational visuals)

**Corporate Communications:**
- **Primary:** Synthesia (professional, multilingual)
- **Alternative:** HeyGen (voice cloning)

**Creative/Artistic Content:**
- **Primary:** Sora (cinematic quality)
- **Specialized:** Seedream + VAYU (tilt-shift effects)
- **Editing:** RunwayML

---

### Step 2: Consider Your Requirements

**Video Length:**
- **5-10 seconds:** Kling
- **30-60 seconds:** Seedream, Kling
- **Up to 60 seconds:** Sora
- **Longer:** Multiple generations + editing

**Resolution:**
- **720p-1080p:** Most tools support
- **1080p:** Sora, Kling
- **Variable:** RunwayML

**Aspect Ratio:**
- **16:9 (landscape):** All tools
- **9:16 (portrait):** Sora, Kling, Seedream
- **1:1 (square):** Sora, Kling

**Budget:**
- **Free tier available:** Kling, RunwayML, HeyGen
- **Subscription required:** Sora, Synthesia
- **Usage-based:** Seedream (via GLIF)

**Skill Level:**
- **Beginner:** Synthesia, HeyGen, Kling
- **Intermediate:** Sora, RunwayML
- **Advanced:** RunwayML (advanced features)

---

### Step 3: Workflow Integration

**Automated Workflows (GLIF):**
- Sora
- Kling
- Seedream + VAYU
- Eleven Labs (voiceover)

**Manual Workflows:**
- Synthesia (template-based)
- HeyGen (avatar-based)
- RunwayML (editing)

**Post-Production Integration:**
- All tools → Premiere Pro, After Effects, CapCut
- Voiceover → Eleven Labs
- Reference images → Midjourney, Stable Diffusion

---

## Integration Planning

### Recommended Tool Combinations

**1. Social Media Content Pipeline:**
```
Kling (text-to-video) → CapCut (editing) → Social Platforms
```

**2. Professional Marketing Video:**
```
Sora (generation) → RunwayML (editing) → Premiere Pro (post-production) → Eleven Labs (voiceover)
```

**3. Automated Documentary Content:**
```
GLIF Workflow:
  - Perplexity (research) → 
  - Seedream (tilt-shift video) → 
  - VAYU (enhancement) → 
  - Eleven Labs (voiceover) → 
  - Final assembly
```

**4. Enterprise Training Video:**
```
Synthesia (avatar + template) → Team review → Distribution
```

**5. Creative Short-Form Content:**
```
Midjourney (reference image) → Sora (image-to-video) → RunwayML (effects) → Final output
```

---

## Best Practices

### Prompt Engineering

**For Text-to-Video (Sora, Kling):**
1. Be specific about camera angles and movements
2. Describe lighting and mood in detail
3. Specify character actions and interactions clearly
4. Include time of day and environmental details
5. Mention desired style (cinematic, documentary, etc.)
6. Keep prompts focused on single clear action
7. Iterate based on outputs to refine prompts

**For Image-to-Video:**
1. Start with high-quality reference image
2. Describe desired motion clearly
3. Specify camera movement (pan, zoom, tracking)
4. Set appropriate duration
5. Review and iterate

**For Avatar Videos (Synthesia, HeyGen):**
1. Select appropriate avatar from library
2. Write clear, natural script
3. Choose appropriate voice (or clone)
4. Use templates for consistency
5. Customize with brand elements

---

### Workflow Optimization

**For Speed:**
- Use Kling for short-form content
- Leverage GLIF automation
- Use templates (Synthesia)
- Batch process when possible

**For Quality:**
- Use Sora for professional content
- Post-process in professional editors
- Add professional voiceovers
- Iterate and refine prompts

**For Cost Efficiency:**
- Start with free tiers (Kling, RunwayML, HeyGen)
- Use GLIF for automated workflows
- Batch similar content
- Optimize video length

---

## Tool Comparison Summary

| Tool | Best For | Video Length | Cost | Skill Level | Integration |
|------|----------|--------------|------|-------------|-------------|
| **Sora** | Professional, cinematic | Up to 60s | Subscription | Beginner-Advanced | GLIF, OpenAI ecosystem |
| **Kling** | Social media, fast | 5-10s | Freemium | Beginner | GLIF, social platforms |
| **RunwayML** | Video editing, effects | Variable | Freemium | Intermediate | API, editing workflows |
| **Synthesia** | Enterprise, training | Variable | $22+/month | Beginner | API, templates |
| **HeyGen** | Avatars, voice cloning | Variable | Freemium | Beginner | API, voice tools |
| **Seedream** | Tilt-shift, creative | 30-60s | Usage-based | Beginner-Intermediate | GLIF, VAYU |
| **VAYU** | Effects enhancement | Variable | Usage-based | Intermediate | GLIF, Seedream |

---

## Next Steps

1. **Identify your primary use case** from the decision framework
2. **Select 2-3 tools** to test based on your requirements
3. **Start with free tiers** where available (Kling, RunwayML, HeyGen)
4. **Set up GLIF workflows** for automation if using multiple tools
5. **Create test videos** to evaluate quality and workflow
6. **Integrate with post-production** tools as needed
7. **Scale successful workflows** for production use

---

## Related Documentation

- **Tools Library:** `../AI_LBS_003_Tools/` - Individual tool JSON files
- **Master Listing:** `../AI_LBS_003_Tools/AI_Tools_Master_Listing.json`
- **GLIF Integration:** `../AI_LBS_003_Tools/GLIF.json` - Workflow automation
- **Eleven Labs:** `../AI_LBS_003_Tools/ElevenLabs.json` - Voiceover integration

---

## Version History

**v1.0** (2025-01-27)
- Initial creation
- Comprehensive tool comparison
- Decision framework
- Integration planning
- Best practices guide

---

**Last Updated:** 2025-01-27  
**Maintained By:** Taxonomy Team  
**Status:** Active

