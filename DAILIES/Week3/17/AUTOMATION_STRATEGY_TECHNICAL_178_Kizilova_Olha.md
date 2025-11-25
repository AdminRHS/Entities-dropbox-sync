# Account Management Automation - Technical Implementation Guide
## Developer Documentation

**Version:** 1.0
**Target Audience:** Developers, DevOps Engineers, Technical Architects
**Last Updated:** 2025-11-18

---

## Table of Contents

1. [Technology Stack](#technology-stack)
2. [Architecture Overview](#architecture-overview)
3. [Automation Workers Implementation](#automation-workers-implementation)
4. [Queue System & Job Processing](#queue-system--job-processing)
5. [AI/ML Integration](#aiml-integration)
6. [Database Triggers & Stored Procedures](#database-triggers--stored-procedures)
7. [API Endpoints](#api-endpoints)
8. [Deployment & Infrastructure](#deployment--infrastructure)
9. [Monitoring & Logging](#monitoring--logging)
10. [Testing Strategy](#testing-strategy)

---

## Technology Stack

### Core Technologies

```yaml
Runtime:
  - Node.js: 18.x LTS
  - TypeScript: 5.x (recommended for type safety)

Backend Framework:
  - Express.js: 4.18.x
  - Sequelize ORM: 6.x

Database:
  - PostgreSQL: 14.x+
  - Redis: 7.x (caching & queues)

Queue System:
  - BullMQ: 4.x (Redis-backed job queues)
  - node-cron: 3.x (scheduled tasks)

AI/ML:
  - OpenAI API (GPT-4) or Anthropic Claude API
  - TensorFlow.js (optional for local ML models)

Notifications:
  - SendGrid (email)
  - Twilio (SMS)
  - Slack SDK (Slack notifications)

Monitoring:
  - Winston (logging)
  - Prometheus (metrics)
  - Grafana (dashboards)
  - Sentry (error tracking)

Testing:
  - Jest: 29.x
  - Supertest: 6.x
  - @faker-js/faker: 8.x

DevOps:
  - Docker & Docker Compose
  - PM2 (process management)
  - Nginx (reverse proxy)
```

### Project Structure

```
account-service/
├── src/
│   ├── config/
│   │   ├── database.ts
│   │   ├── redis.ts
│   │   ├── queues.ts
│   │   └── env.ts
│   ├── models/
│   │   ├── Account.ts
│   │   ├── JobAccount.ts
│   │   ├── Verification.ts
│   │   └── ...
│   ├── workers/
│   │   ├── PasswordRotationWorker.ts
│   │   ├── UsageTrackerWorker.ts
│   │   ├── DocumentExpirationWorker.ts
│   │   ├── SecurityAuditWorker.ts
│   │   ├── SubscriptionRenewalWorker.ts
│   │   ├── EntitiesSyncWorker.ts
│   │   ├── PaymentProcessorWorker.ts
│   │   └── JobPostAutomationWorker.ts
│   ├── ai-engines/
│   │   ├── SuspensionRecommenderAI.ts
│   │   ├── AssignmentIntelligenceAI.ts
│   │   ├── ValidationAI.ts
│   │   └── UsageAnalyzerAI.ts
│   ├── services/
│   │   ├── AccountService.ts
│   │   ├── EntitiesApiService.ts
│   │   ├── EncryptionService.ts
│   │   ├── NotificationService.ts
│   │   └── SyncService.ts
│   ├── queues/
│   │   ├── processors/
│   │   │   ├── passwordRotation.processor.ts
│   │   │   ├── paymentRetry.processor.ts
│   │   │   └── entitiesSync.processor.ts
│   │   └── index.ts
│   ├── middleware/
│   │   ├── usageTracker.ts
│   │   ├── auth.ts
│   │   └── validation.ts
│   ├── cron/
│   │   ├── schedules.ts
│   │   └── jobs.ts
│   ├── utils/
│   │   ├── encryption.ts
│   │   ├── idGenerator.ts
│   │   └── logger.ts
│   └── app.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   ├── migrations/
│   └── seeds/
├── .env.example
├── package.json
├── tsconfig.json
└── README.md
```

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Load Balancer (Nginx)                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │ API      │    │ API      │    │ API      │
    │ Instance │    │ Instance │    │ Instance │
    │ :3000    │    │ :3001    │    │ :3002    │
    └────┬─────┘    └────┬─────┘    └────┬─────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────┐            ┌──────────────────┐
│   PostgreSQL    │            │      Redis       │
│   (Primary DB)  │            │  (Cache+Queue)   │
└─────────────────┘            └──────────────────┘
                                        │
                  ┌─────────────────────┼─────────────────────┐
                  │                     │                     │
                  ▼                     ▼                     ▼
         ┌────────────────┐    ┌────────────────┐   ┌────────────────┐
         │ Worker Pool 1  │    │ Worker Pool 2  │   │ Worker Pool 3  │
         │ (Automation)   │    │ (AI/ML)        │   │ (Sync)         │
         └────────────────┘    └────────────────┘   └────────────────┘
                  │                     │                     │
                  └─────────────────────┼─────────────────────┘
                                        │
                                        ▼
                            ┌────────────────────────┐
                            │   External Services    │
                            │ - SendGrid (Email)     │
                            │ - Twilio (SMS)         │
                            │ - Slack API            │
                            │ - OpenAI/Claude API    │
                            │ - Payment Gateways     │
                            └────────────────────────┘
```

### Automation Flow

```
┌───────────────┐
│   Triggers    │
│               │
│ - Cron Jobs   │
│ - API Events  │
│ - Webhooks    │
│ - Thresholds  │
└───────┬───────┘
        │
        ▼
┌───────────────────┐
│   Queue System    │
│    (BullMQ)       │
│                   │
│ - Job scheduling  │
│ - Retry logic     │
│ - Priority        │
│ - Concurrency     │
└─────────┬─────────┘
          │
          ├─── High Priority Queue
          ├─── Medium Priority Queue
          └─── Low Priority Queue
          │
          ▼
┌─────────────────────────┐
│    Worker Processes     │
│                         │
│ ┌─────────────────────┐ │
│ │ Fully Automated     │ │
│ │ - Run autonomously  │ │
│ │ - No human input    │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ Semi-Automated      │ │
│ │ - Human initiates   │ │
│ │ - System executes   │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ AI-Driven           │ │
│ │ - AI recommends     │ │
│ │ - Human approves    │ │
│ └─────────────────────┘ │
└───────────┬─────────────┘
            │
            ▼
┌───────────────────────────┐
│   Notification System     │
│ - Email                   │
│ - Slack                   │
│ - SMS                     │
│ - In-app                  │
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│   Logging & Monitoring    │
│ - Winston (logs)          │
│ - Prometheus (metrics)    │
│ - Sentry (errors)         │
└───────────────────────────┘
```

---

## Automation Workers Implementation

### 1. Password Rotation Worker

**File:** `src/workers/PasswordRotationWorker.ts`

```typescript
import { Worker, Job } from 'bullmq';
import { Account, PasswordHistory } from '../models';
import { encrypt } from '../utils/encryption';
import { generateSecurePassword } from '../utils/passwordGenerator';
import { notificationService } from '../services/NotificationService';
import { logger } from '../utils/logger';

export class PasswordRotationWorker {
  private worker: Worker;

  constructor() {
    this.worker = new Worker(
      'password-rotation',
      this.processJob.bind(this),
      {
        connection: redisConnection,
        concurrency: 5, // Process 5 passwords concurrently
        limiter: {
          max: 10,
          duration: 60000 // Max 10 per minute
        }
      }
    );

    this.worker.on('completed', (job) => {
      logger.info(`Password rotation completed for account: ${job.data.account_id}`);
    });

    this.worker.on('failed', (job, err) => {
      logger.error(`Password rotation failed for account: ${job?.data.account_id}`, err);
    });
  }

  async processJob(job: Job) {
    const { account_id } = job.data;

    const account = await Account.findByPk(account_id);
    if (!account) {
      throw new Error(`Account ${account_id} not found`);
    }

    // Generate new password
    const newPassword = generateSecurePassword();

    // Store old password in history
    await PasswordHistory.create({
      verifiable_type: 'account',
      verifiable_id: account.id,
      old_pass: account.password,
      change_date: new Date()
    });

    // Update account with new password
    const encryptedPassword = await encrypt(newPassword);
    await account.update({
      password: encryptedPassword,
      security_metadata: {
        ...account.security_metadata,
        password_last_changed: new Date(),
        password_change_required: false
      }
    });

    // Store in secure vault
    await this.storeInVault(account.id, newPassword);

    // Notify owner
    await notificationService.send({
      to: account.owner.email,
      template: 'password_rotated',
      data: {
        account_name: account.name,
        rotation_date: new Date()
      }
    });

    // Log change
    await account.logChange('password_rotated', 'SYSTEM', {
      reason: 'automated_90day_rotation'
    });

    return { account_id, success: true };
  }

  private async storeInVault(accountId: number, password: string) {
    // Integration with secret management system (Vault, AWS Secrets Manager, etc.)
    // For now, store encrypted in separate secure table
    await db.secure_credentials.upsert({
      account_id: accountId,
      credential_type: 'password',
      encrypted_value: await encrypt(password),
      created_at: new Date()
    });
  }
}
```

**Cron Trigger:**

```typescript
// src/cron/schedules.ts
import cron from 'node-cron';
import { Account } from '../models';
import { passwordRotationQueue } from '../queues';

// Daily at 3 AM
cron.schedule('0 3 * * *', async () => {
  const accountsNeedingRotation = await Account.findAll({
    where: sequelize.where(
      sequelize.fn('DATE_DIFF',
        sequelize.literal('CURRENT_DATE'),
        sequelize.col('security_metadata.password_last_changed')
      ),
      { [Op.gte]: 90 }
    )
  });

  for (const account of accountsNeedingRotation) {
    await passwordRotationQueue.add('rotate', { account_id: account.id });
  }

  logger.info(`Queued ${accountsNeedingRotation.length} accounts for password rotation`);
});
```

---

### 2. Usage Tracking Middleware

**File:** `src/middleware/usageTracker.ts`

```typescript
import { Request, Response, NextFunction } from 'express';
import { Account } from '../models';
import { usageAnalyticsQueue } from '../queues';
import { logger } from '../utils/logger';

export const usageTracker = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const accountId = req.params.id || req.body.account_id;

  if (accountId && req.method !== 'GET') {
    // Fire-and-forget async tracking
    setImmediate(async () => {
      try {
        // Increment usage counter
        await Account.increment('usage_count', {
          where: { id: accountId }
        });

        // Update last used timestamp
        await Account.update(
          {
            last_used_at: new Date(),
            'usage_metadata.last_used_date': new Date()
          },
          { where: { id: accountId } }
        );

        // Queue analytics job
        await usageAnalyticsQueue.add('track-usage', {
          account_id: accountId,
          action: req.path,
          method: req.method,
          user_id: req.user.id,
          timestamp: new Date()
        });
      } catch (error) {
        logger.error('Usage tracking failed:', error);
        // Don't fail the request if tracking fails
      }
    });
  }

  next();
};
```

**Usage Analytics Worker:**

```typescript
// src/workers/UsageAnalyticsWorker.ts
import { Worker } from 'bullmq';
import { Account, UsageEvent } from '../models';

export class UsageAnalyticsWorker {
  private worker: Worker;

  constructor() {
    this.worker = new Worker(
      'usage-analytics',
      this.processUsageEvent.bind(this),
      {
        connection: redisConnection,
        concurrency: 10
      }
    );
  }

  async processUsageEvent(job: Job) {
    const { account_id, action, method, user_id, timestamp } = job.data;

    // Store usage event
    await UsageEvent.create({
      account_id,
      action,
      method,
      user_id,
      timestamp
    });

    // Analyze pattern (every 100 events)
    const eventCount = await UsageEvent.count({ where: { account_id } });
    if (eventCount % 100 === 0) {
      await this.analyzeUsagePattern(account_id);
    }
  }

  async analyzeUsagePattern(accountId: number) {
    const last30Days = new Date();
    last30Days.setDate(last30Days.getDate() - 30);

    const events = await UsageEvent.findAll({
      where: {
        account_id: accountId,
        timestamp: { [Op.gte]: last30Days }
      }
    });

    const usageDays = new Set(events.map(e => e.timestamp.toDateString())).size;
    const totalUses = events.length;
    const avgUsesPerDay = totalUses / 30;

    // Determine frequency
    let frequency: string;
    if (usageDays === 0) frequency = 'inactive';
    else if (avgUsesPerDay >= 5) frequency = 'daily';
    else if (usageDays >= 20) frequency = 'weekly';
    else if (usageDays >= 10) frequency = 'monthly';
    else if (usageDays >= 3) frequency = 'quarterly';
    else frequency = 'rarely';

    // Update account metadata
    await Account.update(
      {
        'usage_metadata.usage_frequency': frequency,
        'usage_metadata.monthly_active_tasks': totalUses,
        'usage_metadata.last_analyzed': new Date()
      },
      { where: { id: accountId } }
    );

    // Generate recommendations
    await this.generateRecommendations(accountId, {
      usageDays,
      totalUses,
      frequency
    });
  }

  async generateRecommendations(accountId: number, stats: any) {
    const account = await Account.findByPk(accountId);
    const recommendations = [];

    // Inactive account
    if (stats.frequency === 'inactive' && account.status_id === 'active') {
      recommendations.push({
        type: 'status_change',
        priority: 'medium',
        action: 'Consider archiving inactive account',
        potential_savings: 'Improved security posture'
      });
    }

    // Underutilized premium
    if (account.subscription_type === 'premium' && stats.totalUses < 10) {
      recommendations.push({
        type: 'downgrade',
        priority: 'high',
        action: 'Downgrade to basic plan',
        potential_savings: 'Cost reduction'
      });
    }

    // High usage without automation
    if (stats.totalUses > 100 && !account.integration_prerequisites?.automation_enabled) {
      recommendations.push({
        type: 'automation',
        priority: 'high',
        action: 'Enable API automation',
        potential_savings: 'Time efficiency'
      });
    }

    if (recommendations.length > 0) {
      await account.update({
        'metadata.ai_recommendations': recommendations,
        'metadata.recommendations_generated_at': new Date()
      });
    }
  }
}
```

---

### 3. Document Expiration Monitor

**File:** `src/workers/DocumentExpirationWorker.ts`

```typescript
import { Worker, Job } from 'bullmq';
import { AccountDocument, Account } from '../models';
import { notificationService } from '../services/NotificationService';
import { Op } from 'sequelize';

export class DocumentExpirationWorker {
  async run() {
    const today = new Date();
    const thresholds = {
      urgent: 7,   // days
      warning: 14,
      notice: 30
    };

    const documents = await AccountDocument.findAll({
      where: {
        expiration_date: { [Op.not]: null }
      },
      include: [{ model: Account, include: ['owner'] }]
    });

    for (const doc of documents) {
      const daysUntilExpiration = this.calculateDaysUntil(doc.expiration_date);

      if (daysUntilExpiration < 0) {
        await this.handleExpiredDocument(doc);
      } else if (daysUntilExpiration <= thresholds.urgent) {
        await this.sendAlert(doc, 'urgent', daysUntilExpiration);
      } else if (daysUntilExpiration <= thresholds.warning) {
        await this.sendAlert(doc, 'warning', daysUntilExpiration);
      } else if (daysUntilExpiration <= thresholds.notice) {
        await this.sendAlert(doc, 'notice', daysUntilExpiration);
      }

      // Auto-renewal for renewable types
      if (this.isAutoRenewable(doc.type_id) && daysUntilExpiration <= 30) {
        await this.initiateRenewal(doc);
      }
    }
  }

  private calculateDaysUntil(date: Date): number {
    const today = new Date();
    const diffTime = date.getTime() - today.getTime();
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  }

  private async handleExpiredDocument(doc: AccountDocument) {
    await doc.update({
      metadata: {
        ...doc.metadata,
        expired: true,
        expired_at: new Date()
      }
    });

    if (this.isRequiredDocument(doc.type_id)) {
      await this.recommendAccountSuspension(doc.account, 'required_document_expired');
    }

    await this.sendAlert(doc, 'expired', 0);
    await this.createRenewalTask(doc);
  }

  private async sendAlert(doc: AccountDocument, level: string, daysRemaining: number) {
    const emojis = { urgent: '🔴', warning: '🟠', notice: '🟡', expired: '❌' };

    await notificationService.send({
      to: doc.account.owner.email,
      subject: `${emojis[level]} Document ${level === 'expired' ? 'EXPIRED' : 'Expiring Soon'}: ${doc.type_id}`,
      template: 'document_expiration_alert',
      data: {
        document_type: doc.type_id,
        account_name: doc.account.name,
        expiration_date: doc.expiration_date,
        days_remaining: daysRemaining,
        urgency_level: level
      },
      channels: level === 'urgent' || level === 'expired' ? ['email', 'slack', 'sms'] : ['email']
    });
  }

  private isAutoRenewable(documentType: string): boolean {
    return ['license', 'subscription', 'certificate'].includes(documentType);
  }

  private isRequiredDocument(documentType: string): boolean {
    return ['passport', 'license'].includes(documentType);
  }
}
```

---

## Queue System & Job Processing

### Queue Configuration

**File:** `src/queues/index.ts`

```typescript
import { Queue, QueueOptions } from 'bullmq';
import Redis from 'ioredis';

const connection = new Redis({
  host: process.env.REDIS_HOST || 'localhost',
  port: parseInt(process.env.REDIS_PORT || '6379'),
  maxRetriesPerRequest: null
});

const defaultQueueOptions: QueueOptions = {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 2000
    },
    removeOnComplete: 100, // Keep last 100 completed jobs
    removeOnFail: 500      // Keep last 500 failed jobs
  }
};

// Define all queues
export const passwordRotationQueue = new Queue('password-rotation', defaultQueueOptions);
export const usageAnalyticsQueue = new Queue('usage-analytics', defaultQueueOptions);
export const documentExpirationQueue = new Queue('document-expiration', defaultQueueOptions);
export const securityAuditQueue = new Queue('security-audit', defaultQueueOptions);
export const subscriptionRenewalQueue = new Queue('subscription-renewal', defaultQueueOptions);
export const paymentProcessingQueue = new Queue('payment-processing', {
  ...defaultQueueOptions,
  defaultJobOptions: {
    ...defaultQueueOptions.defaultJobOptions,
    priority: 1, // Highest priority
    attempts: 5   // More retries for payments
  }
});
export const entitiesSyncQueue = new Queue('entities-sync', defaultQueueOptions);
export const aiRecommendationQueue = new Queue('ai-recommendation', defaultQueueOptions);

// Export all queues
export const queues = [
  passwordRotationQueue,
  usageAnalyticsQueue,
  documentExpirationQueue,
  securityAuditQueue,
  subscriptionRenewalQueue,
  paymentProcessingQueue,
  entitiesSyncQueue,
  aiRecommendationQueue
];
```

### Job Processors

**File:** `src/queues/processors/paymentRetry.processor.ts`

```typescript
import { Job } from 'bullmq';
import { VerificationSubscriptionPayment, VerificationSubscription } from '../../models';
import { PaymentGatewayService } from '../../services/PaymentGatewayService';
import { notificationService } from '../../services/NotificationService';
import { logger } from '../../utils/logger';

export async function processPaymentRetry(job: Job) {
  const { payment_id } = job.data;

  const payment = await VerificationSubscriptionPayment.findByPk(payment_id, {
    include: ['subscription']
  });

  if (!payment) {
    throw new Error(`Payment ${payment_id} not found`);
  }

  const retryNumber = payment.retry_count + 1;

  try {
    // Attempt payment
    const paymentGateway = new PaymentGatewayService();
    const result = await paymentGateway.chargeSubscription(
      payment.subscription,
      payment.amount
    );

    // Success - update payment
    await payment.update({
      payment_status: 'completed',
      transaction_id: result.transaction_id,
      metadata: {
        ...payment.metadata,
        retry_count: retryNumber,
        completed_on_retry: retryNumber
      }
    });

    logger.info(`Payment ${payment_id} succeeded on retry ${retryNumber}`);

    // Send receipt
    await notificationService.send({
      to: payment.subscription.owner.email,
      template: 'payment_success',
      data: {
        amount: payment.amount,
        currency: payment.currency,
        receipt_url: result.receipt_url
      }
    });

  } catch (error) {
    await payment.update({
      retry_count: retryNumber,
      payment_status: 'failed',
      notes: error.message
    });

    if (retryNumber >= 3) {
      // All retries failed
      await handlePaymentFailure(payment.subscription, payment);
    } else {
      // Schedule next retry (1, 3, 7 hours)
      const delays = [1, 3, 7];
      const delayHours = delays[retryNumber - 1] || 24;

      await job.queue.add('retry-payment', { payment_id }, {
        delay: delayHours * 60 * 60 * 1000
      });

      logger.info(`Payment ${payment_id} retry ${retryNumber} failed, next retry in ${delayHours} hours`);
    }

    throw error;
  }
}

async function handlePaymentFailure(subscription: VerificationSubscription, payment: any) {
  // Suspend subscription
  await subscription.update({
    status_id: 'suspended',
    suspended_at: new Date(),
    suspension_reason: 'payment_failed_after_retries'
  });

  // Notify user
  await notificationService.send({
    to: subscription.owner.email,
    template: 'payment_failed_final',
    channels: ['email', 'slack'],
    data: {
      subscription_id: subscription.id,
      failed_amount: payment.amount,
      retry_count: payment.retry_count
    }
  });

  // Create manual review task
  await Task.create({
    task_template_id: 'TEMPLATE-TASK-PAYMENT-FAILURE',
    related_entity_type: 'subscription',
    related_entity_id: subscription.id,
    assigned_to: 'FINANCE_TEAM',
    priority: 'high',
    title: `Payment Failed: Subscription ${subscription.id}`,
    status: 'pending'
  });
}
```

---

## AI/ML Integration

### AI Service Configuration

**File:** `src/services/AIService.ts`

```typescript
import Anthropic from '@anthropic-ai/sdk';
import OpenAI from 'openai';

export class AIService {
  private anthropic: Anthropic;
  private openai: OpenAI;

  constructor() {
    this.anthropic = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY
    });

    this.openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY
    });
  }

  async generateWithClaude(prompt: string, systemPrompt?: string): Promise<string> {
    const message = await this.anthropic.messages.create({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 4096,
      system: systemPrompt,
      messages: [
        {
          role: 'user',
          content: prompt
        }
      ]
    });

    return message.content[0].type === 'text' ? message.content[0].text : '';
  }

  async generateWithGPT(prompt: string, systemPrompt?: string): Promise<string> {
    const completion = await this.openai.chat.completions.create({
      model: 'gpt-4-turbo-preview',
      messages: [
        { role: 'system', content: systemPrompt || 'You are a helpful assistant.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      max_tokens: 4096
    });

    return completion.choices[0].message.content || '';
  }

  async analyzeJSON<T>(data: any, analysisType: string): Promise<T> {
    const prompt = `Analyze this ${analysisType} data and return structured JSON:

${JSON.stringify(data, null, 2)}

Return only valid JSON, no markdown or explanation.`;

    const result = await this.generateWithClaude(prompt);

    // Parse JSON from response
    const jsonMatch = result.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      throw new Error('AI did not return valid JSON');
    }

    return JSON.parse(jsonMatch[0]) as T;
  }
}

export const aiService = new AIService();
```

### Suspension Recommender AI Implementation

**File:** `src/ai-engines/SuspensionRecommenderAI.ts`

```typescript
import { Account, SecurityIssue, AccountDocument, Verification } from '../models';
import { aiService } from '../services/AIService';
import { Op } from 'sequelize';

interface SuspensionScore {
  total_score: number;
  max_score: number;
  recommend_suspension: boolean;
  risk_level: 'low' | 'medium' | 'high' | 'critical';
  action: string;
  confidence: number;
  reasons: string[];
  evidence: any[];
}

export class SuspensionRecommenderAI {
  async analyzeAndRecommend(): Promise<any[]> {
    const accounts = await Account.findAll({
      where: { status_id: 'active' },
      include: ['verifications', 'documents', 'owner']
    });

    const recommendations = [];

    for (const account of accounts) {
      const score = await this.calculateSuspensionScore(account);

      if (score.recommend_suspension) {
        recommendations.push({
          account_id: account.id,
          account_name: account.name,
          suspension_score: score.total_score,
          risk_level: score.risk_level,
          reasons: score.reasons,
          recommended_action: score.action,
          confidence: score.confidence,
          evidence: score.evidence
        });
      }
    }

    // Sort by score (highest risk first)
    recommendations.sort((a, b) => b.suspension_score - a.suspension_score);

    // Auto-suspend high-confidence cases
    for (const rec of recommendations) {
      if (rec.confidence >= 0.95 && rec.risk_level === 'critical') {
        await this.autoSuspend(rec);
      } else {
        await this.createReviewTask(rec);
      }
    }

    return recommendations;
  }

  async calculateSuspensionScore(account: Account): Promise<SuspensionScore> {
    let totalScore = 0;
    const reasons: string[] = [];
    const evidence: any[] = [];

    // Factor 1: Inactivity (0-25 points)
    const daysSinceLastUse = this.daysSince(account.last_used_at);
    if (daysSinceLastUse > 180) {
      totalScore += 25;
      reasons.push('Inactive for more than 180 days');
      evidence.push({ factor: 'inactivity', days: daysSinceLastUse, weight: 0.25 });
    } else if (daysSinceLastUse > 90) {
      totalScore += 15;
      reasons.push('Inactive for more than 90 days');
      evidence.push({ factor: 'inactivity', days: daysSinceLastUse, weight: 0.15 });
    }

    // Factor 2: Security Issues (0-30 points)
    const securityIssues = await this.getSecurityIssues(account);
    if (securityIssues.critical > 0) {
      totalScore += 30;
      reasons.push(`${securityIssues.critical} critical security issues`);
      evidence.push({ factor: 'security', issues: securityIssues, weight: 0.30 });
    } else if (securityIssues.high > 0) {
      totalScore += 20;
      reasons.push(`${securityIssues.high} high security issues`);
      evidence.push({ factor: 'security', issues: securityIssues, weight: 0.20 });
    }

    // Factor 3: Expired Documents (0-20 points)
    const expiredDocs = await AccountDocument.count({
      where: {
        account_id: account.id,
        expiration_date: { [Op.lt]: new Date() }
      }
    });
    if (expiredDocs > 0) {
      totalScore += 20;
      reasons.push(`${expiredDocs} expired documents`);
      evidence.push({ factor: 'expired_documents', count: expiredDocs, weight: 0.20 });
    }

    // Factor 4: Failed Verifications (0-15 points)
    const failedVerifications = await Verification.count({
      where: {
        verifiable_type: 'account',
        verifiable_id: account.id,
        verification_status: 'failed'
      }
    });
    if (failedVerifications > 0) {
      totalScore += 15;
      reasons.push(`${failedVerifications} failed verifications`);
      evidence.push({ factor: 'failed_verifications', count: failedVerifications, weight: 0.15 });
    }

    // Factor 5: Terminated Owner (0-10 points)
    if (account.owner?.status === 'terminated') {
      totalScore += 10;
      reasons.push('Account owner terminated');
      evidence.push({ factor: 'owner_terminated', weight: 0.10 });
    }

    // Determine risk level and recommendation
    let riskLevel: 'low' | 'medium' | 'high' | 'critical';
    let action: string;
    let confidence: number;

    if (totalScore >= 80) {
      riskLevel = 'critical';
      action = 'suspend_immediately';
      confidence = 0.95;
    } else if (totalScore >= 60) {
      riskLevel = 'high';
      action = 'suspend_with_review';
      confidence = 0.85;
    } else if (totalScore >= 40) {
      riskLevel = 'medium';
      action = 'flag_for_review';
      confidence = 0.70;
    } else {
      riskLevel = 'low';
      action = 'continue_monitoring';
      confidence = 0.60;
    }

    return {
      total_score: totalScore,
      max_score: 100,
      recommend_suspension: totalScore >= 40,
      risk_level: riskLevel,
      action: action,
      confidence: confidence,
      reasons: reasons,
      evidence: evidence
    };
  }

  private daysSince(date: Date): number {
    if (!date) return 999;
    const today = new Date();
    const diffTime = today.getTime() - date.getTime();
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  }

  private async getSecurityIssues(account: Account) {
    const issues = { critical: 0, high: 0, medium: 0, low: 0 };

    // Check password age
    const passwordAge = this.daysSince(account.security_metadata?.password_last_changed);
    if (passwordAge > 180 && !account.security_metadata?.two_factor_enabled) {
      issues.critical++;
    } else if (passwordAge > 90) {
      issues.high++;
    }

    // Check 2FA
    if (!account.security_metadata?.two_factor_enabled) {
      issues.medium++;
    }

    return issues;
  }

  private async autoSuspend(recommendation: any) {
    const account = await Account.findByPk(recommendation.account_id);

    await account.update({
      status_id: 'suspended',
      'metadata.suspension_reason': 'automated_ai_recommendation',
      'metadata.suspension_score': recommendation.suspension_score,
      'metadata.suspended_at': new Date(),
      'metadata.suspended_by': 'AI_SUSPENSION_ENGINE'
    });

    await account.logChange('auto_suspended', 'AI_SYSTEM', {
      reasons: recommendation.reasons,
      score: recommendation.suspension_score,
      confidence: recommendation.confidence
    });

    await this.notifySuspension(account, recommendation);
  }

  private async notifySuspension(account: Account, recommendation: any) {
    await notificationService.send({
      to: [account.owner.email, 'admin@company.com'],
      subject: `Account Suspended: ${account.name}`,
      template: 'account_auto_suspended',
      channels: ['email', 'slack'],
      data: {
        account_name: account.name,
        suspension_score: recommendation.suspension_score,
        reasons: recommendation.reasons,
        confidence: recommendation.confidence
      }
    });
  }

  private async createReviewTask(recommendation: any) {
    await Task.create({
      task_template_id: 'TEMPLATE-TASK-SUSPENSION-REVIEW',
      related_entity_type: 'account',
      related_entity_id: recommendation.account_id,
      assigned_to: 'OPS_MANAGER',
      priority: recommendation.risk_level === 'high' ? 'high' : 'medium',
      due_date: this.addDays(new Date(), recommendation.risk_level === 'high' ? 1 : 3),
      title: `Review Suspension Recommendation: ${recommendation.account_name}`,
      description: `AI recommends suspending this account. Score: ${recommendation.suspension_score}/100`,
      metadata: { recommendation }
    });
  }

  private addDays(date: Date, days: number): Date {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
  }
}
```

---

(Continuing with Database Triggers, API Endpoints, Deployment, Monitoring, and Testing in next sections...)

**FILE CONTINUES IN NEXT RESPONSE TO AVOID LENGTH LIMITS**
