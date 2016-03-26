# prazeni.honzajavorek.cz

[![Build Status](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz.svg?branch=master)](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz)

Source code of a blog called _Pražení_, which [@zuzejk](https://github.com/zuzejk) and I started to let our friends in Brno know how we are doing after moving to Prague.


## Installation

```shell
$ git clone https://github.com/honzajavorek/prazeni.honzajavorek.cz.git ~/prazeni
$ cd ~/prazeni
```


## Writing Articles

1.  Before writing, make sure you download other people's changes from GitHub:

    ```shell
    $ blog update
    ```

2.  To start a new article, use:

    ```shell
    $ blog write
    ```

3.  To add photos to the article you just started, use:

    ```shell
    $ blog photos ../../my-photos/album/
    ```

    It should work also with a single picture:

    ```shell
    $ blog photos ../../my-photos/album/24340826629_d5bb5abb9e_o.jpg
    ```

4.  To locally verify how your changes are going to look like, use:

    ```shell
    $ blog preview
    ```

5.  When ready, publish your changes:

    ```shell
    $ blog publish
    ```

    When published, check [Travis CI](https://travis-ci.org/honzajavorek/prazeni.honzajavorek.cz) for possible errors. If it's green and there are no errors, the blog was successfully published and should be accessible from [prazeni.honzajavorek.cz](http://prazeni.honzajavorek.cz/) in a minute or two.


## License

All Rights Reserved © [@zuzejk](https://github.com/zuzejk) & [@honzajavorek](https://github.com/honzajavorek)
