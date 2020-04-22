# syntax-parsers

Sample grammars based on the book _Syntactic Theory_ by Sag, Wasow, and Bender.

## Getting Started

The system is designed to be run from within Eclipse or PyCharm, but you should be able to run the grammar by invoking

`$ python3 main.py`

In the app, load the desired grammar file and type in a sample sentence.

```> #load chap_3.fcfg
Parser with grammar "chap_3.fcfg" successfully loaded
> you and chris deny the defendant```

from the src repository. Here, you can load the appropriate grammar and type in sample sentences, which the system will then try to parse.

### Prerequisites

Requires python3 and nltk to run.

### Installing

Installing both python3 and nltk on Windows/Mac: 
https://www.guru99.com/download-install-nltk.html

Intalling python3 on Linux:
https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

Installing nltk for python3 on Linux:
https://askubuntu.com/questions/996185/how-can-i-install-nltk-for-python-3


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
