# prazeni.honzajavorek.cz

[![Build Status](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz.svg?branch=master)](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz)

Source code of a blog called _Pražení_, which [@zuzejk](https://github.com/zuzejk) and I started to let our friends in Brno know how we are doing after moving to Prague.


## Installation

### Windows

Choose location on your disk where the blog is going to live. Let's say `D:\prazeni.honzajavorek.cz`. First, let's go to `D:\`:

```
C:\Users\zuzka> D:
```

Then let's clone this repository:

```
D:\> git clone https://github.com/honzajavorek/prazeni.honzajavorek.cz.git
D:\> cd prazeni.honzajavorek.cz
```

Then let's create a virtualenv folder, activate the virtualenv and then install dependencies:

```
D:\prazeni.honzajavorek.cz> python -m venv venv
D:\prazeni.honzajavorek.cz> venv\Scripts\activate.bat
(venv) D:\prazeni.honzajavorek.cz> pip install -r requirements.txt
```

Now you should be ready. You can test everything works properly by running `blog --help`:

```
(venv) D:\prazeni.honzajavorek.cz> blog --help
```

## Writing Articles

1.  Before writing, make sure you download other people's changes from GitHub:

    ```
    blog update
    ```

2.  To start a new article, use:

    ```
    blog write
    ```

3.  To add photos to the article you just started, use:

    ```
    blog photos ../../my-photos/album/
    ```

    It should work also with a single picture:

    ```
    blog photos ../../my-photos/album/24340826629_d5bb5abb9e_o.jpg
    ```

4.  To locally verify how your changes are going to look like, use:

    ```
    blog preview
    ```

5.  When ready, publish your changes:

    ```
    blog publish
    ```

    When published, check [Travis CI](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz) for possible errors. If it's green and there are no errors, the blog was successfully published and should be accessible from [prazeni.honzajavorek.cz](http://prazeni.honzajavorek.cz/) in a minute or two.


## License

All Rights Reserved © [@zuzejk](https://github.com/zuzejk) & [@honzajavorek](https://github.com/honzajavorek)
