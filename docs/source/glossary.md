---
myst:
  html_meta:
    "description": "Terms and definitions used throughout the Acumbamail integration with Plone documentation."
    "property=og:description": "Terms and definitions used throughout the Acumbamail integration with Plone documentation."
    "property=og:title": "Glossary"
    "keywords": "Plone, Acumbamail, documentation, glossary, term, definition"
---

This glossary provides terms and definitions relevant to **Acumbamail integration with Plone**.

(glossary-label)=

# Glossary

```{glossary}
:sorted: true

Acumbamail
    [Acumbamail](https://acumbamail.com/) is a cloud-based Email Marketing and Marketing Automation platform.
    It provides services such as newsletter management, contact and subscriber management, marketing automation, subscription forms, landing pages, transactional email, SMS campaigns, and campaign analytics.
    When integrated with Plone and Volto, it can be used to collect subscribers, synchronize contacts, automate email campaigns, and personalize communications based on user interactions.

Plone
    [Plone](https://plone.org/) is an open-source content management system that is used to create, edit, and manage digital content, like websites, intranets and custom solutions.
    It comes with over 20 years of growth, optimisations, and refinements.
    The result is a system trusted by governments, universities, businesses, and other organisations all over the world.

Volto
    Volto is the default React-based frontend for Plone 6.
    It communicates with the Plone backend via the REST API.
    The `volto-acumbamail` add-on integrates Acumbamail subscription forms into Volto pages.

    -   [volto-acumbamail](https://github.com/collective/volto-acumbamail)

add-on
    An add-on in Plone extends its functionality.
    It is code that is released as a package to make it easier to install.

    In Volto, an add-on is a JavaScript package.

    In Plone core, an add-on is a Python package.

    -   [Plone core add-ons](https://github.com/collective/awesome-plone#readme)
    -   [Volto add-ons](https://github.com/collective/awesome-volto#readme)
    -   [Add-ons tagged with the trove classifier `Framework :: Plone` on PyPI](https://pypi.org/search/?c=Framework+%3A%3A+Plone)

API Key
    The API Key is a secret token used to authenticate requests from Plone to the Acumbamail API.
    It corresponds to the personal token available at [https://acumbamail.com/api/](https://acumbamail.com/api/).
    It must be stored only in the Plone backend and never exposed to the Volto frontend.

API URL
    The base URL of the Acumbamail API endpoint.
    It is configured in the `Acumbamail Settings` control panel and used by the backend to communicate with the Acumbamail service.

List ID
    A numeric identifier that refers to the Acumbamail mailing list where new subscribers will be added.
    It is configured in the `Acumbamail Settings` control panel.

Subscriber
    A subscriber represents one contact registered in an Acumbamail mailing list.
    Typical fields include email address, name, surname, phone, language, and organization-specific custom fields.

Double Opt-in
    A subscription confirmation workflow recommended for GDPR compliance.
    After submitting the subscription form, the user receives a confirmation email and must click a link to become an active subscriber.
    It improves email list quality, reduces spam complaints, and helps comply with privacy regulations.

Campaign
    An email message or series of messages sent to a group of subscribers in Acumbamail.
    Common types include newsletters, promotions, announcements, and invitations.
    Campaigns are typically created inside Acumbamail and triggered by subscriber synchronization from Plone.

Segment
    A subset of subscribers filtered by specific criteria such as language, location, membership level, or behavior.
    Segments allow personalized communications to be sent to targeted groups.

Custom Fields
    Additional fields defined in Acumbamail to store organization-specific subscriber data beyond the default fields.
    Examples include company, country, department, and membership level.
    These can be synchronized from Plone.

Tag
    A label attached to subscribers in Acumbamail to classify them for automation and personalized campaigns.
    Examples include volunteer, customer, speaker, vip, and donor.

Automation
    An automated workflow in Acumbamail triggered by subscriber events or time intervals.
    A typical example is sending a welcome email after a new subscription, followed by a series of follow-up messages.

Transactional Email
    An email sent automatically in response to a specific user action, as opposed to a bulk campaign.
    Examples include password reset, registration confirmation, purchase confirmation, and invoice delivery.
    These are typically triggered directly from Plone.

GDPR
    General Data Protection Regulation. A European Union regulation on data protection and privacy.
    When collecting subscribers, it is recommended to implement explicit consent, a privacy policy link, Double Opt-in, and the right to unsubscribe and to delete subscriber data.

plone.restapi
    [plone.restapi](https://plonerestapi.readthedocs.io/) is a RESTful hypermedia API for Plone.
    It is used by `collective.volto.acumbamail` to expose the `@acumbamail-settings` and `@acumbamail-subscribe` endpoints to the Volto frontend.

@acumbamail-settings
    A REST API endpoint exposed by `collective.volto.acumbamail` that provides the Acumbamail configuration settings to the Volto frontend.
    Anonymous users cannot access the Plone registry directly, so this dedicated endpoint is used instead.

@acumbamail-subscribe
    A REST API endpoint exposed by `collective.volto.acumbamail` that allows Volto to add a new subscriber to the configured Acumbamail list.
    It wraps the [addSubscriber](https://acumbamail.com/apidoc/function/addSubscriber/) Acumbamail API function.

    Example:

    ```shell
    curl -i -X POST http://localhost:8080/Plone/@acumbamail-subscribe \
      -H "Accept: application/json" \
      -H "Accept-Language: es" \
      --data '{"email": "user@example.com"}'
    ```

addSubscriber
    The Acumbamail API function used to add a new contact to a mailing list.
    Full documentation at [https://acumbamail.com/apidoc/function/addSubscriber/](https://acumbamail.com/apidoc/function/addSubscriber/).

Control Panel
    The `Acumbamail Settings` configuration panel available in Plone's Site Setup under `Add-on Configuration`.
    It allows administrators to configure the `API URL`, `API Key`, and `List ID` fields stored in `plone.registry`.

plone.registry
    A Plone component that stores configuration values as named records.
    `collective.volto.acumbamail` uses it to persist the `IAcumbamailSettings` interface fields (`api_url`, `api_key`, `list_id`).

GenericSetup
    A Plone framework for managing configuration through filesystem-based import and export profiles.
    `collective.volto.acumbamail` uses a GenericSetup profile to register its registry records and control panel on installation.

Markedly Structured Text
MyST
    [Markedly Structured Text (MyST)](https://myst-parser.readthedocs.io/en/latest/) is a rich and extensible flavor of Markdown, for authoring Plone Documentation.
    The documentation of this project is written in MyST.

Sphinx
    [Sphinx](https://www.sphinx-doc.org/en/master/) is a tool that makes it easy to create intelligent and beautiful documentation.
    It was originally created for Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.
    It can generate multiple output formats, including HTML and PDF, from a single source.

```
