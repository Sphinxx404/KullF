import os
import time
import pyfiglet
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

def web_scraper():
  os.system("cls" if os.name=="nt" else "clear")
  
  print(Fore.BLUE + pyfiglet.figlet_format("K U L L F"))  
  print("\tVersion 2.0\t</Z3r0X>\n\n======== [M E N U] =======\n")
  
  print(Fore.GREEN + "1. Find Website Source Code")
  print(Fore.GREEN + "2. Find Headers")
  print(Fore.GREEN + "3. Find Links")
  print(Fore.GREEN + "4. Exit")
   
  try:
      cmd = int(input(Fore.CYAN + "\n(kullf)" + " " +Fore.WHITE +"> "))
  except ValueError:
      print(Fore.RED + "\n[!] Invalid option.")
      exit()
  
  if cmd == 1:
      url = input("\nEnter URL of target website: ").strip()
      if not url.startswith("http"):
          url = "http://" + url
      try:
          response = requests.get(url)
          response.raise_for_status()
          soup = BeautifulSoup(response.text, "html5lib")
          print(Fore.YELLOW + f'\n[*] Pulling Source Code for {url}, please wait...\n')
          time.sleep(4)
          print(soup.prettify())
  
          try:
              with open("source_code.txt", "a", encoding="utf-8") as codeFile:
                  codeFile.write(soup.prettify() + "\n\n")
              print(Fore.YELLOW + "[+] Source code saved to source_code.txt")
          except Exception as e:
              print(Fore.RED + f"\n[!] Error while saving the file:\n{e}")
  
      except requests.exceptions.RequestException as e:
          print(Fore.RED + f"[!] Failed to fetch the URL:\n{e}")
          exit()
  
  elif cmd == 2:
      url = input("\nEnter URL of target website: ").strip()
      if not url.startswith("http"):
          url = "http://" + url
      try:
          response = requests.get(url)
          response.raise_for_status()
          soup = BeautifulSoup(response.text, "html5lib")
  
          h1 = [tag.text.strip() for tag in soup.find_all("h1")]
          h2 = [tag.text.strip() for tag in soup.find_all("h2")]
          h3 = [tag.text.strip() for tag in soup.find_all("h3")]
          h4 = [tag.text.strip() for tag in soup.find_all("h4")]
          h5 = [tag.text.strip() for tag in soup.find_all("h5")]
          h6 = [tag.text.strip() for tag in soup.find_all("h6")]
  
          print("\nH1 Headers:", h1)
          print("H2 Headers:", h2)
          print("H3 Headers:", h3)
          print("H4 Headers:", h4)
          print("H5 Headers:", h5)
          print("H6 Headers:", h6)
  
          try:
              with open("headers.txt", "a", encoding="utf-8") as codeFile:
                  codeFile.write("H1: " + str(h1) + "\n")
                  codeFile.write("H2: " + str(h2) + "\n")
                  codeFile.write("H3: " + str(h3) + "\n")
                  codeFile.write("H4: " + str(h4) + "\n")
                  codeFile.write("H5: " + str(h5) + "\n")
                  codeFile.write("H6: " + str(h6) + "\n\n")
              print(Fore.YELLOW + "[+] Headers saved to headers.txt")
          except Exception as e:
              print(Fore.RED + f"\n[!] Error while saving headers:\n{e}")
  
      except requests.exceptions.RequestException as e:
          print(Fore.RED + f"\n[!] Failed to fetch the URL:\n{e}")
          exit()
  
  elif cmd == 3:
      url = input("\nEnter URL of target website: ").strip()
      if not url.startswith("http"):
          url = "http://" + url
      try:
          response = requests.get(url)
          response.raise_for_status()
          soup = BeautifulSoup(response.text, "html5lib")
          links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
  
          if not links:
              print(Fore.RED + "[!] No links found.")
              exit()
  
          print(Fore.YELLOW + f"\n[*] Pulling Links from {url}...\n")
          for link in links:
              print(link)
  
          try:
              with open("links.txt", "a", encoding="utf-8") as codeFile:
                  codeFile.write("\n".join(links) + "\n\n")
              print(Fore.YELLOW + "[+] Links saved to links.txt")
          except Exception as e:
              print(Fore.RED + f"\n[!] Error while saving links:\n{e}")
  
      except requests.exceptions.RequestException as e:
          print(Fore.RED + f"\n[!] Failed to fetch the URL:\n{e}")
          exit()
  
  elif cmd == 4:
      print(Fore.CYAN + "\n[+] Thanks for using...\n")
      exit()
  else:
      print(Fore.RED + "\n[!] Invalid choice.")
      
web_scraper()
