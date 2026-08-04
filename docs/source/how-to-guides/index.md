---
myst:
  html_meta:
    "description": "Acumbamail integration with Plone how-to guides"
    "property=og:description": "Acumbamail integration with Plone how-to guides"
    "property=og:title": "Acumbamail integration with Plone how-to guides"
    "keywords": "Acumbamail, service, Plone, integration, documentation, how-to, guides"
---

# General information

This part of the documentation contains how-to guides, and including installation and usage.

## Features

- Control panel in {term}`Plone` registry to manage {term}`Acumbamail Settings`.

- A Restricted RESTful API endpoint that exposes the {term}`Acumbamail Settings` for {term}`Volto` _integration_.

- A Restricted RESTful API endpoint that support the {term}`Acumbamail`'s {term}`batchAddSubscribers` endpoint to add a new subscriber to the list.

## Volto integration

To use this product in {term}`Volto`, you needs to include the following {term}`add-on`
in your project: {term}`volto-acumbamail`.

## Translations

This product support the following languages:

- Basque

- Catalan

- English

- Galician

- Spanish

## Compatibility

- Tested with `Python` 3.12 and {term}`Plone` 6.1.5.

## Install it

To install in your project, the {term}`collective.volto.acumbamail` {term}`add-on` with `pip` command:

```shell
pip install collective.volto.acumbamail
```

## Enable it

Visit http://localhost:8080/Plone in a browser, login, so go to `Site setup`, next to `Add-ons` control panel, 
find the {term}`collective.volto.acumbamail` {term}`add-on` and select the `Install` button for enabled it.

## Settings it

To use this {term}`add-on`, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="Add-on Configuration" src="../images/addon-configuration-acumbamail-icon.png">

This {term}`Acumbamail Settings`, you can access the control panel, as shown below:

<img width="720" alt="Acumbamail Settings" src="../images/acumbamail-settings.png">

In this control panel, you can configure the following fields:

- {term}`API URL`, The address of the {term}`Acumbamail` API endpoint.

- {term}`API Key`, Your personal token generated at the {term}`Acumbamail` Dashboard website.

- {term}`List ID`, Numeric identifier of the subscribers list.

## Use it

To use the {term}`Acumbamail` integration you need add the {term}`volto-acumbamail` {term}`add-on`, in
your {term}`Volto` project and use the amazing features into this {term}`add-on`.
