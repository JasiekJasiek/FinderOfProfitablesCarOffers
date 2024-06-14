# Finder of profitable car offers
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
  
## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>

  This project is result of the cooperation between two high school friends, <b>Jan Szala</b> and <b>Szymon Mierzwicki</b>. <br />
  Our goal was to simplify process of looking for a new car. This program is scaning "otomoto.pl" for new offers <br />
  and when finds one, it will decide if this founded offer is in some way worth to check. <br />
  What's more same program will sent you an e-mail with link to this offer and some statistical charts

</details>

## Technologies

  <details>
<summary>Click here to see used technologies!</summary>

  <ul>
<li>python 3.12.1</li>
<li>BeautifulSoup</li>
<li>requests</li>    
<li>matplotlib</li>
<li>sqlite3</li>    
<li>smtplib</li>
<li>ssl</li>
  </ul>

</details>

## Setup

<details>
<summary>Click here to see how to setup!</summary>

### Installation on Windows

* Download and install `Python 3.12.1`

    ```
    https://www.python.org/downloads/release/python-3100/
    ```
* Download this repository and unzip


* Create python virtual environment

```bash
py -m venv venv
```

* Active python virtual environment

```bash
venv\Scripts\activate
```

* Install require packages

```bash
pip install -r Requirements.txt
```

### Installation on Linux/Macos

* Download and install `Python 3.12.1`

    ```
    https://www.python.org/downloads/release/python-3100/
    ```
* Download this repository and unzip


* Create python virtual environment

```bash
python3 -m venv venv
```

* Active python virtual environment

```bash
. venv/bin/activate
```

* Install require packages

```bash
pip install -r Requirements.txt
```

### Usage

* For start you should run <br />

```bash
initiate.py
``` 

to make database <b>(it could take over 3 days to colect all data)</b>, it will store all cars atribute which are put up for sale, program needs it for evalute new offers. <br /> <br />
We provie database, <b>but it might be outdated</b>. <br />
* To start scanning "otomoto.pl" you should run the <br />

```bash
main.py
``` 

and let it run in the background<br />
</details>
