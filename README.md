<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FrancisTembo/libbot">
    <img src="images/photo.webp" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NWU Library Chatbot 🤖</h3>

  <p align="center">
    Chatbot assistant for the North-West University's Library!
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installing-requirements">Installing Requirements</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is the project home for NWU's library chatbot. The chatbot encapsulates the natural language understanding component of the physical robotic assistant found in the library. 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This project was developed and tested on Ubuntu 20.04

* Install 
  ```sh
  sudo apt update
  sudo apt install python3
  ```

### Installing Requirements

1. Clone the repo - make sure you have the correct access
   ```sh
   git clone https://github.com/FrancisTembo/libbot.git
   cd libbot
   ```
2. Install poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```
4. Install dependancies:
   ```sh
   poetry install
   ```
5. Activate poetry environment
   ```sh
   poetry shell

<!-- USAGE EXAMPLES -->
## Usage

1. Train the Rasa assistant
   ```python
   rasa train
   ```
2. Starting the bot in the terminal
   ```python
   rasa shell
   ```

<!-- ROADMAP -->
## Roadmap

- [x] Implementing current library FAQ.
- [x] Add `Telegram`  channel.
- [ ] Add speech to text interface.


<!-- LICENSE -->
## License

This repository belongs to the North-West University LIbrary

<!-- CONTACT -->
## Contact

Francis Tembo: francistembo92@gmail.com
