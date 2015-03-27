#!/usr/bin/perl

#-------------------------------------------------
$ver = "採用フォーム用";# メールフォーム
$my_home = "http://www.j-quest.jp/";
#-------------------------------------------------
#  設定項目
#-------------------------------------------------

require './mimew.pl'; 
use Jcode; 
use Encode;
use MIME::Base64;

# スクリプト名
$script = './mail.cgi';

# sendmailパス
$sendmail = '/usr/sbin/sendmail'; 

# メールアドレス
$my_mail = 'suzukinobufumi@mbg.ocn.ne.jp';

# 複数のメルアドを記す場合は、''の中に記して「,」でつなぐ。
@mail_g = ('recruit@jqst.jp','nobusuzuki@pse.or.jp',);

# タイトル
$title = "お問合せフォーム";

# 最大送信文字数（半角文字数500→全角250文字。''で無制限。）
$c_max = '';

# 確認画面を表示(0=NO 1=YES)
$confirmation = '1';

# 自動返信メール(0=NO 1=YES)
$r_mail = '0';  

# 自動返信メールの文章
#「@ 」と「" 」はそれぞれ「 \@」、「　\" 」と記する。
$r_msg = "

この度はお問い合せ頂き誠にありがとうございました。
担当者より、ご連絡をさせて頂きます。
このメールに心当たりの無い場合は、お手数ですが下記連絡先までお問い合わせください。

この度はお問い合わせ重ねてお礼申し上げます。

J-Quest

今後とも宜しくお願い致します。

"; 

# 送信後のhtml
$t_mail = 'thankyou.html'; 

# 入力必須項目 ['フィールド名','表示名'],… という形式で必須項目の数だけ記述する。
# たとえば、フォームで
#       電話番号：<input type='text' name="電話" value="">
# という箇所があり、これを必須項目にする場合には、
# @inputCheck = (
#	['電話','電話番号']
# );
# という風に記述する。
# 複数の必須項目を記す場合は「,」でつなぐ。
# 必須項目がない場合は、@inputCheck = (); とする。
@inputCheck = (
	['email','Eメール'],

);

# 確認用メールとの整合性チェック(1=YES 0=NO)
$MAIL_CHECK = 1; 

# メールフィールド名、確認用メールフィールド名
@MAIL_FIELDS_NAME = ('email','email2');  

#------------------設定ここまで-------------------

#-------------------------------------------------
# デコード処理
#-------------------------------------------------
&decode2;
if($orden eq 'send' || $confirmation == '0'){ &send; }
&Conf;
sub decode2{
if ($ENV{'REQUEST_METHOD'} eq "POST"){
	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	}else{ &error("サーバーエラー"); }
@pairs = split(/&/,$buffer);
foreach $pair (@pairs) {
	($key,$value) = split(/=/,$pair);
	$key =~ tr/+/ /;
	$key =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
	$value =~ s/\r\n/\n/g;
	$value =~ s/\r/\n/g;
	$value =~ s/&/&amp;/g;
	$value =~ s/"/&quot;/g;
	$value =~ s/</&lt;/g;
	$value =~ s/>/&gt;/g;
	&Jcode'convert(*key,'utf8');
	&Jcode'convert(*value,'utf8');

if($key ne 'location' && $key ne 'orden' && $key ne 'subject'){
	$temp = "$key \= $value\n\n";
	$contenido = $contenido.$temp;
	&Jcode'h2z_utf8(*contenido) if($hankana == '1');
push(@pre_key, $key);
push(@pre_value, $value);}
if($c_max && length($value) > $c_max){ 
	&error("文字数が制限をこえています"); }
$in{$key} = $value;} 
$orden = $in{'orden'};

#-------------------------------------------------
# 入力チェック
#-------------------------------------------------
$subject = $in{'subject'};
$name = $in{'名前'};
$email = $in{'email'};
if(!$name || $name =~ /(,|\n|\r|\t|;|:|<)/){
	&error("名前が未入力です"); }
if($email !~ /^[-\.\w]+\@[a-zA-Z0-9][-\.\w]+\.[a-zA-Z]{2,4}$/){ 
	&error("Ｅメールが正しくありません"); }
if($orden ne 'send' && $MAIL_CHECK) {
	$chkMail = $in{$MAIL_FIELDS_NAME[0]};
	$chkMail2 = $in{$MAIL_FIELDS_NAME[1]};
if ($chkMail ne $chkMail2) {
  	&error("確認用メールアドレスと一致しません");}}
foreach $no(0 .. $#inputCheck) {
	$chkName = $inputCheck[$no]->[0];
	$chkLabel = $inputCheck[$no]->[1];
if ($in{$chkName} eq "") { &error("$chkLabel が未記入です"); }}
}

#-------------------------------------------------
# 事前確認
#-------------------------------------------------
sub Conf {
&Jcode'convert(*subject,'utf8');
&head;
	print "<form action=\"$script\" method=post>\n";
	print "<div align=\"center\"><div class=\"style2\">$subject確認画面</div><table border=0 cellpadding=3 cellspacing=3>\n";
$num = @pre_key;
foreach(0..$num-1){
if ($pre_key[$_] ne $MAIL_FIELDS_NAME[1]) {
  	print "<tr>\n\t";
  	print "<td class=\"style\" align=right width=20% nowrap>";
  	print "$pre_key[$_]";
  	print "</td>\n";
  	print "<td width=80%>";
	$infor = $pre_value[$_];
  	&Jcode'convert(*infor,'utf8');
  	print "$infor";
  	print "</td></tr>\n";}}
	print "</table></div>\n";
foreach(0..$num-1){
if ($pre_key[$_] ne $MAIL_FIELDS_NAME[1]) {
	print "<input type=\"hidden\" name=\"$pre_key[$_]\" value=\"$pre_value[$_]\">\n";}}
	print "<input type=hidden name=subject value=\"$subject\">\n";
	print "<input type=hidden name=location value=\"$t_mail\">\n";
	print "<input type=hidden name=orden value=send>\n";
	print "<br><p align=center><input type=\"button\" value=\"戻る\" onClick=\"history.back()\">&nbsp;<input type=submit value=\"送　信\"></form></p>\n";
	print "<p align=center><a href=$my_home target=_blank>$ver</a></p>\n";
	print "</body>\n";
	print "</html>\n";
	exit;
}

#-------------------------------------------------
# 送信処理
#-------------------------------------------------
sub send {
if($email =~ /(,|　|\s|;|:|<)/ || $subject =~ /(,|\n|\t|\r|;|:|<)/ || $my_mail =~ /(,|　|\s|;|:|<)/ ){
	&error("サーバーエラー");}
	&Jcode'convert(*contenido,'utf8');
	&Jcode'convert(*subject,'utf8');
	$subject = encode_base64($subject,"");
	$subject = "=?utf-8?B?" . $subject . "?=";
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
if ($host eq "" || $host eq "$addr") { 
	$host = gethostbyaddr(pack('C4', split(/\./, $addr)), 2) || $addr; 
		}
if ($host eq "") { $host = $addr; }
foreach(@mail_g){
if($_ && $_ !~ /(,|　|\s|;|:|<)/ ){
	open(MAIL,"|$sendmail -t") || die &error("サーバーエラー"); 
	print MAIL  encode("MIME-Header", "Reply-To: $email")."\n";
	print MAIL encode("MIME-Header","To: $_")."\n";
	print MAIL encode("MIME-Header","From: $email")."\n";
	print MAIL "Subject: $subject\n";
	print MAIL "Content-Transfer-Encoding: 64bit\n";
	print MAIL "Content-Type: text/plain\; charset=UTF-8\n\n";
	print MAIL "$contenido\n\n";

if (!close(MAIL)){ 
	&error("サーバーエラー"); }}
} 

#-------------------------------------------------
# 自動返信処理
#-------------------------------------------------
if($r_mail == '1'){
	&Jcode'convert(*res_msg,'utf8');
	open(MAIL,"|$sendmail -t") || die &error("サーバーエラー"); 
	print MAIL encode("MIME-Header","Reply-To: $my_mail")."\n";
	print MAIL encode("MIME-Header","To: $email")."\n";
	print MAIL encode("MIME-Header","From: $my_mail")."\n";
	print MAIL "Subject: $subject\n";
	print MAIL "Content-Transfer-Encoding: 64bit\n";
	print MAIL "Content-Type: text/plain\; charset=UTF-8\n\n";
	print MAIL "$r_msg";
	print MAIL "===================================================\n";
	print MAIL "$contenido\n\n";
	print MAIL "===================================================\n";
if (!close(MAIL)){ &error("サーバーエラー"); }} 
	print "Location: $t_mail\n";
	print "Content-type: text/html;charset=utf8\n\n";
	exit;

} 

#-------------------------------------------------
# ヘッダー
#-------------------------------------------------
sub head {
	print "Content-type: text/html\n\n";
	print <<"EOM";
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>$title</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<style type="text/css">
	<!--
	* {
	font-family: "ＭＳ Ｐゴシック", "Hiragino Kaku Gothic Pro W3", "ヒラギノ角ゴ Pro W3", "Osaka";
	font-size: 15px;
	color: #000000;
	}
	body {
	margin: 100px;
	margin-top: 50px;
	}
	table {
	border:solid 1px #156646;
	width: 500px;
	}
	.style {
	color: #1566467;
	}
	.style2 {
	font-size: 15px;
	font-weight: bold;
	padding-bottom: 15px;
	-->
	</style>
	</head>
EOM
}

#-------------------------------------------------
# エラー処理
#-------------------------------------------------
sub error{
local($atencion) = @_;
	&head;
	print "<div align=center>";
	print "<p class=\"style\">$atencion</p><br><br>";
	print "<input type=\"button\" value=\"戻る\" onClick=\"history.back()\">";
	print "</div></body></html>";
	exit;
}
