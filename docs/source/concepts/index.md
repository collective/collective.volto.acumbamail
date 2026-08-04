---
myst:
  html_meta:
    "description": "Acumbamail Plone concepts"
    "property=og:description": "Acumbamail integration with Plone concepts"
    "property=og:title": "Acumbamail integration with Plone concepts"
    "keywords": "Acumbamail, service, Plone, integration, documentation, concepts"
---

# Functional concepts

Functional concepts of integration with {term}`Acumbamail` service in {term}`Plone` and {term}`Volto`.

## Overview

{term}`Acumbamail` is a cloud-based Email Marketing and Marketing Automation platform that provides services such as:

- Newsletter management
- Contact and subscriber management
- Marketing automation
- Subscription forms
- Landing pages
- Transactional email
- SMS campaigns
- Campaign analytics

When integrated with {term}`Plone` and {term}`Volto`, {term}`Acumbamail` can implements to collect subscribers, synchronize contacts, automate email campaigns, and personalize communications based on user interactions.

---

# Architecture

```text
                    +----------------------+
                    |      Volto UI        |
                    | (React Frontend)     |
                    +----------+-----------+
                               |
                               | REST API
                               |
                    +----------v-----------+
                    |       Plone          |
                    |  Business Logic      |
                    +----------+-----------+
                               |
                     HTTP REST API
                               |
                    +----------v-----------+
                    |     Acumbamail API   |
                    +----------+-----------+
                               |
                 Email Marketing Platform
```

---

# Main concepts

## 1. Account

The {term}`Acumbamail` account represents the organization using the service.

It contains:

- Mailing lists
- Subscribers
- Campaigns
- Forms
- Automation workflows
- Statistics

---

## 2. The API key

The API Key is using to authenticate requests from {term}`Plone`.

Example:

```
Authorization: Bearer YOUR_API_KEY
```

Recommendations:

- Never expose it in {term}`Volto`.
- Store it only in the Plone backend.
- Load it from environment variables.

Example:

```bash
ACUMBAMAIL_API_KEY=xxxxxxxxxxxxxxxx
```

---

## 3. Lists

A List is a collection of subscribers.

Examples:

- Newsletter
- Customers
- Events
- Employees

Typical operations:

- Create subscriber
- Remove subscriber
- Update subscriber
- Query subscriber

Example

```
Newsletter Subscribers
```

---

## 4. Subscribers

A subscriber represents one contact.

Typical fields

| Field | Description |
|---------|-------------|
| email | Email address |
| name | Full name |
| surname | Last name |
| phone | Optional phone |
| language | Preferred language |
| custom fields | Organization-specific data |

Example

```json
{
  "email": "john@example.com",
  "name": "John",
  "surname": "Doe"
}
```

---

## 5. Double opt-in

Recommended for `GDPR` compliance.

Workflow

```
User
 ↓
Subscription Form
 ↓
Confirmation Email
 ↓
User Confirms
 ↓
Subscriber becomes Active
```

Advantages

- Better email quality
- `GDPR` compliance
- Lower spam complaints

---

## 6. Forms

{term}`Acumbamail` lets the creation of subscription forms.

With Plone there are two approaches.

### Embedded form

Using {term}`Acumbamail` HTML.

Pros

- It's easy to implement

Cons

- Limited customization

---

### Native Plone form

Preferred.

Workflow

```
Volto Form
        ↓
REST API
        ↓
Plone
        ↓
Acumbamail API
```

Advantages

- Better UX
- Validation
- Security
- Analytics
- Integration with workflows

---

# Campaigns

Campaigns are email messages sent to subscribers.

Possible campaign types

- Newsletter
- Promotions
- Announcements
- Invitations

Campaign creation is usually performed directly inside {term}`Acumbamail`.

Plone normally triggers subscriber synchronization.

---

# Segments

Subscribers can dividing into segments.

Examples

```
Customers

Employees

Spanish speakers

Premium users

Event attendees
```

Useful for personalized communications.

---

# Custom fields

Custom fields store organization-specific information.

Example

| Field |
|---------|
| Company |
| Country |
| Department |
| Membership Level |

These can be synchronizing from {term}`Plone`.

---

# Tags

Tags classify subscribers.

Examples

```
volunteer

customer

speaker

vip

donor
```

Useful for automation.

---

# Automation

{term}`Acumbamail` supports automated workflows.

Example

```
New subscriber
        ↓
Welcome email
        ↓
Wait 3 days
        ↓
Send resources
        ↓
Wait 7 days
        ↓
Request feedback
```

---

# Transactional emails

Different from campaigns.

Examples

- Password reset
- Registration confirmation
- Purchase confirmation
- Invoice delivery

These are typically triggered directly from {term}`Plone`.

---

# Statistics

{term}`Acumbamail` provides metrics such as

- Delivered
- Open rate
- Click rate
- Bounce rate
- Unsubscribe rate

These statistics can be displaying inside {term}`Plone` if desired.

---

# Integration patterns

## Pattern 1

Newsletter Subscription

```
Volto Form

↓

Plone REST Endpoint

↓

Acumbamail API

↓

Subscriber Added
```

---

## Pattern 2

Registration Synchronization

```
User Registration

↓

Plone User Created

↓

Subscriber Created

↓

Welcome Automation
```

---

## Pattern 3

CRM Synchronization

```
CRM

↓

Plone

↓

Acumbamail
```

---

# REST integration

Typical backend flow

```
Volto

↓

POST /newsletter

↓

Plone REST Service

↓

Acumbamail API

↓

Response

↓

Volto
```

---

# JSON payload example

```json
{
  "email": "user@example.com",
  "name": "John",
  "surname": "Doe",
  "list": "Newsletter"
}
```

---

# Error handling

Common validations

- Invalid email
- Already subscribed
- Invalid API key
- Rate limit exceeded
- Network timeout

Backend should return meaningful messages.

---

# Security recommendations

## Never expose the API Key

Correct

```
Volto

↓

Plone

↓

Acumbamail
```

Incorrect

```
Volto

↓

Acumbamail
```

---

## Validate input

Validate

- email
- required fields
- duplicates

before calling the API.

---

## HTTPS

Always communicate using HTTPS.

---

## Logging

Log

- successful subscriptions
- failed requests
- API errors

Avoid logging API keys.

---

# GDPR considerations

Recommended

- Explicit consent checkbox
- Privacy policy link
- Double Opt-in
- Right to unsubscribe
- Right to delete subscriber
- Consent timestamp

---

# Suggested Plone components

Possible implementation

```
acumbamail/
│
├── browser/
├── services/
├── subscribers/
├── adapters/
├── interfaces.py
├── api.py
├── utils.py
└── configure.zcml
```

---

# Suggested Volto components

```
src/
│
├── components/
│     └── NewsletterForm
│
├── hooks/
│
├── services/
│
├── helpers/
│
└── config/
```

---

# Recommended workflow

```
Visitor

↓

Volto Newsletter Block

↓

Plone REST Endpoint

↓

Validation

↓

Acumbamail

↓

Subscriber Created

↓

Confirmation Message
```

---

# Best practices

- Keep the API key only in Plone.
- Use REST services for communication.
- Implement Double Opt-in.
- Handle duplicate subscriptions.
- Synchronize custom fields.
- Log integration errors.
- Retry transient API failures.
- Monitor API rate limits.
- Use asynchronous tasks for bulk synchronization.
- Follow `GDPR` and local privacy regulations.

---

# References

Please checkout the {ref}`general-resources-label` section for more details.
