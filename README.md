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

Then let's create a virtualenv folder and activate the virtualenv:

```
D:\prazeni.honzajavorek.cz> python -m venv venv
D:\prazeni.honzajavorek.cz> venv\Scripts\activate.bat
```

Now we need to install dependencies. Because Windows are the most ridiculous OS on the planet, you can't just install whatever is in the `requirements.txt` file by `pip`. You need to:

1.  Make sure you have the latest `pip`. It's important.

    ```
    (venv) D:\prazeni.honzajavorek.cz> python -m pip install pip --upgrade
    ```

2.  Manually download the `lxml` library in form of a *wheel* from [this unofficial registry](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml). Choose version appropriate for your Python and OS versions (e.g. `cp35` means Python 3.5, `win32` means 32bit OS). Then install it inside your virtualenv:

    ```
    (venv) D:\prazeni.honzajavorek.cz> pip install lxml-3.6.0-cp35-cp35m-win32.whl
    ```

3.  Now proceed with standard installation:

    ```
    (venv) D:\prazeni.honzajavorek.cz> pip install -r requirements.txt
    ```

If everything went correctly, you should be ready at this point. You can test everything works properly by running `blog --help`:

```
(venv) D:\prazeni.honzajavorek.cz> blog --help
```

## Writing Articles

1.  Before using the blog, you need to go to the directory where it lives and activate virtualenv.
    If `blog --help` doesn't work, then you're ready yet.

2.  Before writing, make sure you download other people's changes from GitHub:

    ```
    blog update
    ```

3.  To start a new article, use:

    ```
    blog write
    ```

4.  To add photos to the article you just started, use:

    ```
    blog photos ../../my-photos/album/
    ```

    It should work also with a single picture:

    ```
    blog photos ../../my-photos/album/24340826629_d5bb5abb9e_o.jpg
    ```

5.  To locally verify how your changes are going to look like, use:

    ```
    blog preview
    ```

6.  When ready, publish your changes:

    ```
    blog publish
    ```

    When published, check [Travis CI](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz) for possible errors. If it's green and there are no errors, the blog was successfully published and should be accessible from [prazeni.honzajavorek.cz](http://prazeni.honzajavorek.cz/) in a minute or two.


## License

All Rights Reserved © [@zuzejk](https://github.com/zuzejk) & [@honzajavorek](https://github.com/honzajavorek)
