---
myst:
  html_meta:
    "description": "Terms and definitions used throughout the Acumbamail integration with Plone documentation."
    "property=og:description": "Terms and definitions used throughout the Acumbamail integration with Plone documentation."
    "property=og:title": "Glossary"
    "keywords": "Acumbamail, service, Plone, integration, documentation, glossary, term, definition"
---

This glossary provides terms and definitions relevant to {term}`Acumbamail` integration with {term}`Plone`.

(glossary-label)=

# Glossary

```{glossary}
:sorted: true

Acumbamail
    [Acumbamail](https://acumbamail.com/) is a cloud-based Email Marketing and Marketing Automation platform.
    It provides services such as newsletter management, contact and subscriber management, marketing automation,
    subscription forms, landing pages, transactional email, SMS campaigns, and campaign analytics.
    When integrated with {term}`Plone` and {term}`Volto`, it can be used to collect subscribers, synchronize contacts, automate
    email campaigns, and personalize communications based on user interactions.

Plone
    [Plone](https://plone.org/) is an open-source content management system that is used to create, edit, and
    manage digital content, like websites, intranets and custom solutions. It comes with over 20 years of growth,
    optimisations, and refinements. The result is a system trusted by governments, universities, businesses, and
    other organisations all over the world.

Volto
    [Volto](https://github.com/plone/volto) is the default React-based frontend for {term}`Plone` 6.
    It communicates with the {term}`Plone` backend via exclusively through the {term}`plone.restapi` REST API.
    The {term}`volto-acumbamail` {term}`add-on` integrates {term}`Acumbamail` subscription forms into {term}`Volto` pages.

add-on
    An add-on in {term}`Plone` extends its core functionality.
    It is distributed as a Python package and installed via the {term}`Plone` Site Setup.
    {term}`collective.volto.acumbamail` is a {term}`Plone` add-on.

    Its companion {term}`volto-acumbamail` is a {term}`Volto` (JavaScript) add-on.

    In {term}`Volto`, an add-on is a JavaScript package.

    In {term}`Plone` core, an add-on is a Python package.

    -   [Plone core add-ons](https://github.com/collective/awesome-plone#readme)
    -   [Volto add-ons](https://github.com/collective/awesome-volto#readme)
    -   [Add-ons tagged with the trove classifier `Framework :: Plone` on PyPI](https://pypi.org/search/?c=Framework+%3A%3A+Plone)

plone.restapi
    [plone.restapi](https://plonerestapi.readthedocs.io/) is the RESTful hypermedia API for {term}`Plone`.
    It enables {term}`Volto` and other clients to interact with {term}`Plone` content and configuration over HTTP using JSON.
    This {term}`add-on` registers its services and control panel adapters through ``plone.restapi``.
    It is used by {term}`collective.volto.acumbamail` to expose the {term}`@acumbamail-settings` and {term}`@acumbamail-subscribe`
    endpoints to the {term}`Volto` frontend.

Control Panel
    Checkout the {term}`Acumbamail Settings` term.

Acumbamail Settings
    The `Acumbamail Settings` configuration panel available in {term}`Plone`'s Site Setup under `Add-on Configuration`.
    It allows administrators to configure the {term}`API URL`, {term}`API Key`, and {term}`List ID` fields stored in {term}`plone.registry`.

plone.registry
    A {term}`Plone` component that stores configuration values as named records.
    {term}`collective.volto.acumbamail` uses it to persist the {term}`IAcumbamailSettings` interface fields ({term}`api_url`, {term}`api_key`, {term}`list_id`).

Registry
    The {term}`Plone` Registry is a key-value store for site configuration, managed by the {term}`plone.registry` package.
    Settings are declared through Zope schema interfaces and stored as typed records.
    In this {term}`add-on` the records are declared in {term}`IAcumbamailSettings` and stored under the ``acumbamail`` prefix (e.g. ``acumbamail.list_id``).
    They can be read using ``plone.api.portal.get_registry_record("acumbamail.list_id")``.

GenericSetup
    A {term}`Plone` framework for managing configuration through filesystem-based import and export profiles.
    {term}`collective.volto.acumbamail` uses a GenericSetup profile to register its registry records and control panel on installation.

collective.volto.acumbamail
    `collective.volto.acumbamail` is the {term}`Plone` {term}`add-on` that integrates {term}`Acumbamail` sevice into a {term}`Plone` site.
    It provides a control panel to configure the {term}`Acumbamail Settings` integration, a REST API endpoint to to add a new contact to
    a mailing list, and a browser layer ({term}`IAcumbamailLayer`) to scope its components.
    It is designed to work together with the {term}`volto-acumbamail` {term}`Volto` {term}`add-on`.

volto-acumbamail
    `volto-acumbamail` is the {term}`Volto` {term}`add-on` that integrates {term}`Acumbamail` sevice into a {term}`Plone` site via the {term}`collective.volto.acumbamail` {term}`add-on`.
    It provides a control panel to configure the target municipality.

    **Tip:** More infomation checkout the official [documentation](https://volto-acumbamail.readthedocs.io/).

IAcumbamailLayer
    ``IAcumbamailLayer`` is a browser layer marker interface provided by this {term}`add-on`.
    It is applied to the request when the {term}`add-on` is installed, scoping all views, services, and adapters to sites where the {term}`add-on` is active.

IAcumbamailSettings
    ``IAcumbamailSettings`` is the Zope schema interface that declares the configuration fields for the {term}`Acumbamail` {term}`add-on`.
    Currently it defines the fields ({term}`api_url`, {term}`api_key`, {term}`list_id`).
    It is used as the schema for both the {term}`Acumbamail Settings` control panel and the {term}`Plone` {term}`Registry` records.

API URL
api_url
    The base URL of the {term}`Acumbamail` API endpoint.
    It is configured in the {term}`Acumbamail Settings` control panel and used by the backend to communicate with the {term}`Acumbamail` service.

API Key
api_key
    The API Key is a secret token used to authenticate requests from {term}`Plone` to the {term}`Acumbamail` API.
    It corresponds to the personal token available at [https://acumbamail.com/api/](https://acumbamail.com/api/).
    It must be stored only in the {term}`Plone` backend and never exposed to the {term}`Volto` frontend.

List ID
list_id
    A numeric identifier that refers to the {term}`Acumbamail` mailing list where new subscribers will be added.
    It is configured in the {term}`Acumbamail Settings` control panel.

@acumbamail-settings
    A REST API endpoint exposed by {term}`collective.volto.acumbamail` that provides the {term}`Acumbamail Settings` to the {term}`Volto` frontend.
    Anonymous users cannot access the {term}`Plone` registry directly, so this dedicated endpoint is used instead.

    **Example:** Take a look to the {ref}`acumbamail-settings-route` section.

@acumbamail-subscribe
    A REST API endpoint exposed by {term}`collective.volto.acumbamail` that allows {term}`Volto` to add a new subscriber to the configured {term}`Acumbamail` list.
    It wraps the [addSubscriber](https://acumbamail.com/apidoc/function/addSubscriber/) {term}`Acumbamail` API function.

    **Example:** Take a look to the {ref}`acumbamail-subscribe-route` section.

addSubscriber
    The {term}`Acumbamail` API function used to add a new contact to a mailing list.

    **Tip:** More infomation checkout the official [addSubscriber/](https://acumbamail.com/apidoc/function/addSubscriber/) documentation.

Subscriber
    A subscriber represents one contact registered in an {term}`Acumbamail` mailing list.
    Typical fields include email address, name, surname, phone, language, and organization-specific custom fields.

Double Opt-in
    A subscription confirmation workflow recommended for GDPR compliance.
    After submitting the subscription form, the user receives a confirmation email and must click a link to become an active subscriber.
    It improves email list quality, reduces spam complaints, and helps comply with privacy regulations.

Campaign
    An email message or series of messages sent to a group of subscribers in {term}`Acumbamail`.
    Common types include newsletters, promotions, announcements, and invitations.
    Campaigns are typically created inside {term}`Acumbamail` and triggered by subscriber synchronization from {term}`Plone`.

Segment
    A subset of subscribers filtered by specific criteria such as language, location, membership level, or behavior.
    Segments allow personalized communications to be sent to targeted groups.

Custom Fields
    Additional fields defined in {term}`Acumbamail` to store organization-specific subscriber data beyond the default fields.
    Examples include company, country, department, and membership level.
    These can be synchronized from {term}`Plone`.

Tag
    A label attached to subscribers in {term}`Acumbamail` to classify them for automation and personalized campaigns.
    Examples include volunteer, customer, speaker, vip, and donor.

Automation
    An automated workflow in {term}`Acumbamail` triggered by subscriber events or time intervals.
    A typical example is sending a welcome email after a new subscription, followed by a series of follow-up messages.

Transactional Email
    An email sent automatically in response to a specific user action, as opposed to a bulk campaign.
    Examples include password reset, registration confirmation, purchase confirmation, and invoice delivery.
    These are typically triggered directly from {term}`Plone`.

GDPR
    General Data Protection Regulation. A European Union regulation on data protection and privacy.
    When collecting subscribers, it is recommended to implement explicit consent, a privacy policy link, Double Opt-in, and the right to unsubscribe and to delete subscriber data.

```
