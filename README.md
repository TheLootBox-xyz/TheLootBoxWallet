# TheLootBoxWallet (README update in progress)

TheLootBoxWallet is an Ethereum wallet that runs locally on your desktop with a focus on privacy and security. A lockbox for your ethereum assets powered by Toga and coffee .

---

### Features

- Account wallet credentials are stored encrypted and decrypted only when the client is in use and unlocked by the account key.

- Create multiple accounts

- Send Ether 

- Lookup other addresses if multiple were created

- Runs locally as a self-contained stand-alone application.

- Soon to be cross-platform thanks to BeeWare.

---

### Install from .deb file release

#### Steps to install

- Download the deb file from the latest release.

https://github.com/TheLootBox-xyz/TheLootBoxWallet/releases

- Run the install command.

`sudo dpkg -i thelootboxwallet-release`

- Start thelootboxwallet from ``.

---

### Setup from source

I highly recommended creating a virtual environment to avoid dependency conflicts.

`python3 -m venv envname`

Once the venv is created source it in order to install the dependencies to that environment.

`source path/to/envname/bin/activate`

---

### Customize default settings

You can customize the default network and ethereum account with a `config.ini` file. If you don't have a `config.ini` file TheLootBoxWallet will use the first public address created as the default address.

Example `config.ini` file:

```bash
[DEFAULT]

network = https://goerli-rollup.arbitrum.io/rpc
default_address = your_public_ethereum_address
```

### Preview screenshot

![TheLootBoxClient](.src/TheLootBoxWallet/code/static/images/TheLootBoxClient.png)

### Community

Join the Discord! https://discord.gg/pd4wupphDe 

### Supporting development

Updating.

### Check out BeeWare

This cross-platform app was generated by `Briefcase` part of
`The BeeWare Project`. If you want to see more tools like Briefcase, please
consider becoming a financial member of BeeWare.

`Briefcase`: https://briefcase.readthedocs.io/
`The BeeWare Project`: https://beeware.org/
`becoming a financial member of BeeWare`: https://beeware.org/contributing/membership
