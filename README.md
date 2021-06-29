# Landlordotron Discord Bot

## Introduction and Purpose

This is a Discord bot I'm writing for my personal Discord server. The joke is that it's the landlord for my server, so it collects rent from tenants (other users), and kicks/bans them if they dont pay their rent after a month. After 15 days, it sends a reminder to pay rent in the general channel.

As this is such a lightweight bot, I plan on running this code off of a headless Raspberry Pi Zero. Functionality may be expanded, if I find new/interesting things to implement.

## Technology Used (So far)

### Software

* Discord API
* Python

### Hardware

* Raspberry Pi Zero (2017)

## Command List

* **!hello** - Standard greeting, no functionality.
* **!rent** - Checks to see if tenant has paid rent for the month. Scolds if tenant has not paid.
* **!payRent** - Pays rent for user, stored for a month before reset.
* **!domey** - Links to https://moutonmerch.com/

## Plans for later

* Actually taking peoples money via Paypal
