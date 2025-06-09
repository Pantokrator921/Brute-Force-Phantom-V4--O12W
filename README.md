![phantomV4](https://github.com/user-attachments/assets/322ed35b-744b-4a27-aa0b-71b655d39e97)
# Phantom Bot - Random Seed Phrase Generator & Checker

This script attempts to find an active Phantom Wallet through pure chance. It continuously generates valid 12-word seed phrases, imports them into Phantom, and checks if they have a balance.

## ⚠️ EXTREME WARNING: The Impossibility of a Random Find

**The probability of finding a wallet with a balance using this script is astronomically low and practically impossible.**

* There are 2048¹² (or 2¹³²) possible 12-word combinations. That's a number with 40 digits.
* Even if you ran this script for millions of years on thousands of computers, your chances of success would be close to zero.

**This script is for purely experimental and educational purposes** to demonstrate how BIP-39 phrases and the security of crypto wallets work. Do **not** expect to find money with it. Think of it as a lottery with unimaginably low odds.

## How It Works

1.  **Infinite Loop:** The script runs forever until stopped manually (`Ctrl+C`).
2.  **Random Phrase Generation:** In each loop, the script uses cryptographically secure methods to generate a **brand new, random, but valid 12-word seed phrase**. It uses the `mnemonic` library, which automatically ensures the correct checksum.
3.  **Automated Import:** The generated phrase is entered into Phantom.
4.  **Balance Check:** The script checks if the imported wallet has a balance greater than $0.00.
5.  **Saves on Success:** In the extremely unlikely event of a find, the seed phrase and balance are saved to the **`found_wallets.txt`** file, and the script continues running.

## Prerequisites

* Python 3.x
* Google Chrome Browser
* ChromeDriver (matching your Chrome version)
* The `.crx` file of the Phantom Wallet extension

## Installation Guide

1.  **Install Dependencies:** This script requires a new library. Install both with this command:
    ```bash
    pip install selenium mnemonic
    ```
    **Note:** The `english.txt` file from previous scripts is **no longer needed**.

2.  **Set up ChromeDriver and `.crx` File:** Follow the instructions from the previous `README` files to prepare ChromeDriver and the Phantom extension file.

3.  **Configure the Script:**
    Open `phantomBot_Random.py` and edit **only one variable**:
    * **`EXTENSION_PATH`**: Enter the absolute path to your Phantom `.crx` file. **No seed words** need to be entered.

## Execution

1.  Run the script from your terminal:
    ```bash
    python phantomBot_Random.py
    ```
2.  The script will now run in an infinite loop. You will see the rate of attempts per second.
3.  **To stop the script, press `Ctrl+C` in the terminal.**![phantomV4](https://github.com/user-attachments/assets/7a0235d9-e4cf-43e0-acd3-c3a3c27defa3)
