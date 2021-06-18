# Landlordotron Discord Bot

## Introduction and Purpose

This is a Discord bot I'm writing for my personal Discord server. The joke is that it's the landlord for my server, so it collects rent from tenants (other users), and kicks/bans them if they dont pay their rent after a month. after 15 days, it sends a reminder to pay rent in the general channel. As this is such a lightweight bot, I plan on running this code off of a headless Raspberry Pi Zero. I might add more functionality as I see fit, or if I get bored.

## Technology Used (So far)

* Discord API
* Python

## Command List

* **!hello** - Standard greeting, no functionality.
* **!rent** - Checks to see if tenant has paid rent for the month. Scolds if tenant has not paid.
* **!payRent** - Pays rent for user, stored for a month before reset.
* **!domey** - Links to https://moutonmerch.com/

## Plans for later

* Actually taking peoples money via Paypal
