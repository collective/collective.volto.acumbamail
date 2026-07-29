---
myst:
  html_meta:
    "description": "Acumbamail integration with Plone how-to guides"
    "property=og:description": "Acumbamail integration with Plone how-to guides"
    "property=og:title": "Acumbamail integration with Plone how-to guides"
    "keywords": "Acumbamail, service, Plone, integration, documentation, how-to, guides"
---

# General information

This part of the documentation contains how-to guides, including installation and usage.

## Features

- Control panel in {term}`Plone` registry to manage {term}`Acumbamail Settings`.

- RestApi endpoint that exposes the {term}`Acumbamail Settings` for {term}`Volto` _integration_.

- Add {term}`batchAddSubscribers` endpoint support to new subscriber to the {term}`Acumbamail` list.

## Volto integration

To use this product in {term}`Volto`, you needs to include the following {term}`add-on` in your project: {term}`volto-acumbamail`.

## Translations

This product has been translated into

- Basque

- Catalan

- English

- Galician

- Spanish

## Compatibility

- Tested with Python 3.12 and {term}`Plone` 6.1.5.

## Install it

Install {term}`collective.volto.acumbamail` with `pip`:

```shell
pip install collective.volto.acumbamail
```

## Enable it

Go to the `Site setup`, next to the `Add-ons` control panel, find the {term}`collective.volto.acumbamail` {term}`add-on` and click on the `Install` button.

Visit http://localhost:8080/ in a browser, login, create a {term}`Plone` site, enabled the {term}`add-on` and check the awesome new features.

## Settings it

To use this {term}`add-on`, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="Add-on Configuration" src="../images/addon-configuration-acumbamail-icon.png">

This {term}`Acumbamail Settings`, you can access the control panel, as shown below:

<img width="720" alt="Acumbamail Settings" src="../images/acumbamail-settings.png">

In this control panel, you can configure the following fields:

- {term}`API URL`, The URL of the {term}`Acumbamail` API endpoint.

- {term}`API Key`, Your personal token generated at the {term}`Acumbamail` Dashboard website.

- {term}`List ID`, Numeric identifier of the list where subscribers will be added.

## Use it

To use the {term}`Acumbamail` integration you need add the {term}`volto-acumbamail` {term}`add-on`, in your {term}`Volto` project and
use the amazain features incluided.
