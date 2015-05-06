<?php include 'php/lib.php'?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <!-- viewport -->
    <meta name="viewport" content="width=device-width initial-scale=1">
    <meta name="keywords" content="JX日鉱日石エネルギー、エネオス、ENEOS、J-Quest、ジェイ･クエスト、ガソリンスタンド、コンビニエンスストア、セルフ給油" />
    <meta name="description" content="全国に81店舗のショッピングモール併設型ガソリンスタンドを運営するJ-Quest（ジェイ･クエストのウェブサイト。企業コンセプト、店舗情報、商品・サービスの紹介、セルフガソリンスタンド、セルフ洗車のご利用方法、採用情報をご覧いただけます。" />
    <meta name="author" content="J-Quest" />
    <meta name="copyright" content="J-Quest" />
    <title>J-Quest（ジェイ･クエスト）のウェブサイト</title>
    <!-- link -->
    <link rel="alternate" type="application/rss+xml" title="ROR" href="ror.xml" />
    <link rel="contents" href="index.html" title="ホーム" />
    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />
    <!-- bootstrap -->
    <link rel="stylesheet" type="text/css" href="bower_components/bootstrap/dist/css/bootstrap.min.css" />
    <!--[if !IE]><!-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <!--<![endif]-->
    <!--[if lte IE 8]>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <![endif]-->
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
      <script src="js/selectivizr-min.js"></script>
      <script src="bower_components/respond/dest/respond.min.js"></script>
    <![endif]-->
    <!--[if gt IE 8]>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <![endif]-->
    <!-- stylesheet -->
    <link rel="stylesheet" type="text/css" href="css/base.css" />
    <!-- bootstrap -->
    <script type="text/javascript" src="bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- flickity -->
    <link rel="stylesheet" media="screen" href="bower_components/flickity/css/flickity.css">
    <script type="text/javascript" src="bower_components/flickity/dist/flickity.pkgd.min.js"></script>
    <script src="js/rollover2.js"></script>
    <script src="php/hbs.js"></script>
    <script src="php/script.js?2"></script>
    <script src="js/script.js"></script>
</head>

<body>
    <!-- navbar -->
    <div class="navbar-container">
        <?php tpl('navbar.hbs');?>
    </div>
    <!-- /navbar -->
    <!--container-->
    <div id="container">
        <div id="headline">&nbsp;</div>
        <h1>J-Quest全国に80店舗。ショッピングモール併設型セルフ方式ガソリンスタンドを運営しております。</h1>
        <!--header-->
        <div id="header" class="hidden-sm hidden-xs">
            <a href="index.html"><img src="images/logo.png" alt="J-Quest" /></a>
        </div>
        <!--/header-->
        <!--contents-->
        <div id="contents" class="container">
            <!--cover-->
            <div class="row visible-md visible-lg">
                <div class="col-md-12">
                    <div id="cover">
                        <img src="images/c_concept.jpg" alt="企業コンセプト" />
                    </div>
                </div>
            </div>
            <!--/<cover-->
            <div class="row row-panel">
                <div class="col-panel col-md-3 hidden-sm hidden-xs">
                    <!--side-->
                    <div id="side"><?php tpl('sideNav.hbs');?></div>
                    <!--/side-->
                </div>
                <div class="col-panel col-md-9 col-sm-12 col-xs-12">
                    <!--main-->
                    <div id="main"><?php main();?></div>
                    <!--/main-->
                </div>
            </div>
        </div>
        <!--/contents-->
        <!--footer-nav-->
        <div class="footer-container">
        <?php tpl('footer.hbs');?>
        </div>
        <!--/footer-nav-->
        <!--上へ戻るボタン-->
        <div id="return_top" class="hidden-xs">
            <a href="#top">&nbsp;</a>
        </div>
        <!--/上へ戻るボタン-->
    </div>
    <!--/container-->
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-29774849-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();
    </script>
</body>

</html>
