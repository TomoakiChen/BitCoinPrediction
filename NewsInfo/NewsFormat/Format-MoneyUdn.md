* 新聞清單
  * 外層
    ```html
    <ul class="story-list-holder">
      <li class="story-headline-wrapper">
        ...
      </li>
    </ul>
    ```  


  * 內層(一條新聞)
    ```html
    <li class="story-headline-wrapper">
      <div class="story__image">
        <a href="https://money.udn.com/money/story/122381/5857536">
          <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/11/01/realtime/14454949.jpg&amp;s=Y&amp;x=47&amp;y=0&amp;sw=1185&amp;sh=790&amp;exp=3600" alt="news photo">
        </a>
      </div>
      <div class="story__content">
        <a href="https://money.udn.com/money/story/122381/5857536">
          <h3 class="story__headline">
            <u>比特幣</u>
            期貨ETF上市 買進前留意這幾個陷阱                  
          </h3>
          <p class="story__text">
            股票投資人現在可能正在羨慕加密貨幣的投資人。加密貨幣中規模最大的<u>比特幣</u>，在10月下旬一度比9月結束時暴漲50%，衝上6.7萬美元價位，創歷史新高，現在多頭甚至認為，<u>比特幣</u>挑戰10萬美元價位指日可待。...                  
          </p>
        </a>
        <time>
          11/02 10:36
        </time>
      </div>
    </li>
    ```

* 新聞內容
  ```html
  <section class="article-main">
              <div class="article-layout-wrapper">
              <article class=""> <!-- add .paywall for paywall article, add .paywall-freebies member free article -->
                  <section class="article-body">
                  <p class="article-length">本文共1854字</p>
                  	<section class="article-keyword">
	<ul class="article-keyword__list">
					<li class="article-keyword__item">
		<a href="/search/tagging/1001/馬斯克" rel="145331">馬斯克</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/半導體" rel="94683">半導體</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/惠宇" rel="152325">惠宇</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/磊晶片" rel="95770">磊晶片</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/元宇宙" rel="176948">元宇宙</a>
		</li>
			</ul>
</section>
<!-- Loction：temp_new/inc/content/story/article_tag -->                  <section class="article-body__social-bar">
                      <ul class="social-bar__list">
                      <li class="social-bar__item">
                          <a href="#" class="fb">
                          <i class="i-facebook-1" title="分享FACEBOOK"></i>
                          </a>
                      </li>
                      <li class="social-bar__item">
                          <a href="#" class="line">
                          <i class="i-line" title="分享LINE"></i>
                          </a>
                      </li>
                      <li class="social-bar__item">
                          <a href="#" class="bookmark">
                          <i class="i-bookmark" title="收藏"></i>
                          </a>
                      </li>
                      <li class="social-bar__item">
                          <a href="#" class="fontsize">
                          <i class="i-text-size" title="調整字形大小"></i>
                          </a>
                      </li>
                      <li class="social-bar__item">
                          <a href="#" class="msg">
                          <i class="i-talk" title="留言"></i>
                          </a>
                      </li>
                                            <li class="social-bar__item" style="display: none;">
                                                <!-- Circular Player -->
                          <div class="circularPlayer">
                          <svg viewBox="0 0 100 100" id="playable" version="1.1" xmlns="http://www.w3.org/2000/svg" width="36" height="36" data-play="playable" class="playable paused">',
                              '<g class="shape">',
                              '<circle class="progress-track" cx="50" cy="50" r="47.45" stroke="#ACACAC" stroke-opacity="1" stroke-linecap="round" fill="none" stroke-width="2"></circle>',
                              '<circle class="progress-bar" cx="50" cy="50" r="47.45" stroke="#D72C1D" stroke-opacity="1" stroke-linecap="round" fill="none" stroke-width="2" transform="rotate(-90 50 50)"></circle>',
                              '</g>',
                              '<circle class="controls toggle" cx="50" cy="50" r="45" stroke="none" fill="#000000" opacity="0.0" pointer-events="all"></circle>',
                              '<g class="control pause">',
                              '<line x1="40" y1="35" x2="40" y2="65" stroke="#D72C1D" fill="none" stroke-width="8" stroke-linecap="round"></line>',
                              '<line x1="60" y1="35" x2="60" y2="65" stroke="#D72C1D" fill="none" stroke-width="8" stroke-linecap="round"></line>',
                              '</g>',
                              '<g class="control play">',
                              '<polygon points="40,30 70,50 40,70" fill="#D72C1D" stroke-width="0"></polygon>',
                              '</g>',
                              '</svg>
                          </div>
                          <!-- Circular Player / -->
                      </li>
                      <!-- mp -->
                      <!-- 隱藏的 player -->
                      <audio class="mp-hide" preload="none">
                          <source src="https://artts.udn.com.tw/edn/5859426-TTS-rebecca.mp3">
                      </audio>

                      <!-- 外層的樣式 -->
                                            <div id="mp" class="mp" style="display: none;">
                                                <div class="mp__wrapper">
                          <div class="mp__progress-track">
                              <div class="mp__progress-bar">
                              <div class="mp__progress-circle"></div>
                              </div>
                          </div>
                          <div class="mp__total-time">00:00</div>
                          </div>
                      </div>
                      <!-- mp -->
                      </ul>
                  </section>
                  <time class="article-body__time">2021/11/02 01:26</time>
                  <div class="info-sharebar-wrapper">
                      <div class="article-body__info">
                          <span>萬寶週刊 撰文/楊惠宇</span>
                      </div>
                      <ul class="article-body__sharebar">
                      <div class="fbbtn">
                      <li class="fblike">
                          <div id="fb-root"></div>
                          <div></div>
                        </li>
                      </div>
                      </ul>
                  </div>
                  <section class="article-body__editor" id="article_body">
                      <!-- cms body start -->
                      <p>
</p><p>
***本文所提之個股內容僅供參考，不具投資建議，投資前應審慎評估風險，且自負盈虧</p><!--1--><p>
</p><p>
萬寶投顧楊惠宇表示，美股雖有通膨問題未解，但在強勁財報下還是處於高檔，Fed即將開會，市場先反應預期，20年及30年殖利率首度出現倒掛，顯示市場擔心緊縮將導致成長放緩，美國第三季GDP年增只有2%，是一年來最差，在離充份就業還有差距下，聯準會迫於通膨會有緊縮動作，但不致於掐住脖子，所以影響不大，不過蘋果、英特爾或亞馬遜都因為缺料及漲價使得財報不如預期，很多個股在第四季動能會減弱，所以在選股上思維要做些改變。</p><div class="only_mobile"><!-- /129853887/udn.com/money/Mobile/300*250-inline -->
<style>.inline-ad { position: relative; overflow: hidden; box-sizing: border-box; }
.inline-ad div { margin: auto; text-align: center; }
.inline-ad iframe { margin: auto; display: block; /*width: auto !important;*/ }
.inline-ad div[id^=google_ads_iframe] {
 padding: 50px 0 30px !important; box-sizing: border-box; height: auto !important;
}

.before_Amnet {
    font-size:18px;
    color:#999;
    text-align:left;
    border-top: 1px solid #d9d9d9;
    width: 100%;
    position:  relative;
    top: 20px;
    left: 0;
    margin:15px 0 15px;
    display:none;
}
.after_Amnet {
    color:#999;
    border-top: 1px solid #d9d9d9;
    width: 100%;
    position: relative;
    bottom: -10px;
    left: 0;
    display:none;
    margin:15px 0 15px;
}
.innity-apps-reset { padding: 20px 0 0 !important; margin: -20px auto -10px !important; }
</style>

<div id="before" class="before_Amnet">推薦</div>

<div class="inline-ad">
<div id="div-gpt-ad-1533623914338-0" align="center" style="margin:0px auto 10px;"></div>
</div>

<div id="after" class="after_Amnet"></div></div><!--2--><p>
 </p><p>
狂人馬斯克1天資產暴增超過1兆台幣，成為全球頭版新聞，根據最近統計他的淨資產高達7.99兆台幣，這樣講或許還沒有什麼概念，中國恒大地產危機一度引起市場恐慌，當時傳言將衍生成為2008年後的新金融危機，而恒大總負債金額為8.4兆台幣，換句話說一個人的馬斯克可以救恒大這隻龐大的地產怪獸，大家在讚嘆之餘，或許可以想想，從馬斯克身上透露出何種商機？</p><!--3--><p>
 </p><p>
講到馬斯克當然大家第一個想到的是特斯拉，然而特斯拉的價值並不僅僅只是在於電池發動，軟實力也是一大重點，想想你的車經過複雜路口時，車輛會自動減速慢行，遇到前方有車會自動變道、還有停車很困難？車子會自動幫你停好，這些「自動駕駛」功能，不僅讓汽車更有溫度，同時「訂閱制」也為特斯拉帶來巨大金流，而要做到自動駕駛，光靠5G尚不夠，還需要「低軌衛星」才能完美無縫接軌，於是SpaceX應運而生，這一切都在馬斯克的計劃之中。</p><!--4--><p>
 </p><p>
關於電動車題材，之前出過一系列的發文，有興趣的投資朋友可上網搜尋，時至今日，許多電動車股也一一發動，最強勢當屬電池系列，康普、美琪瑪、聚和紛紛創下新高，其中康普的券資比雖然沒有另外兩檔多，但短期內也急速上升，「題材、營收、軋空」三種合起聲勢驚人，當然這些股票都很好，但在連續大漲加上萬七有壓下，不免也讓人有點膽戰心驚，那麼或許可以往低基期的題材股來尋找。</p><!--5--><p>
 </p><p>
長園科主要產品應用於電池模組及不斷電系統等方面，營運方面雖然尚未見起色，但對比同樣虧損狀態的立凱大漲創高下，或有題材拉升效應。</p><!--6--><p>
 </p><p>
萬寶投顧楊惠宇指出，低軌衛星除在5G時代為互補功用，但到了6G時代則將與各種傳輸技術及通訊系統和毫米波進一步融合，換句話地位將更為重要，馬斯克自六年前展開「星鏈Starlink計劃」為的就是可以提供全球Wi-Fi服務，目前已經發射1800顆低軌衛星，最後計劃將有12,000顆衛星環繞全球，換句話說目前滲透率只有15%，未來仍有龐大商機。</p><!--7--><p>
 </p><p>
未來為因應大量終端裝置連網需求，頻寬、高頻為趨勢，所以地面衛星天線及各種小型基地台將密集分佈，要提升相關射頻元件材料性能，第三代半導體為不可或缺角色。</p><!--8--><p>
 </p><p>
全新具研發、生產及製造半導體磊晶片能力，砷化鎵晶圓及磊晶全球市占25%位居第二，在3D感測VCSEL車用需求增加下，上半年獲利2.45元己接近去年全年水準。除第二代半導體發展穩定外，在第三代半導體部份GaN on SiC磊晶己打入台系國防工業供應鏈，通過認證小量出貨，至於5G基地台部分，也於美系IDM廠認證中，此外宏捷科為其客戶，未來或許有望因此順勢切入中美晶之第三代半導體供應鏈中。</p><!--9--><p>
 </p><p>
萬寶投顧楊惠宇強調，除了電動車、低軌衛星外，馬斯克另一代表為「加密貨幣」，比特幣、狗狗幣及以太幣皆為其收藏，加密貨幣的重要精神為「區塊鏈技術」，去中心化及不可篡改性使得這些虛擬產品得到安全保障，FB更名為「Meta」，積極奔向「元宇宙」，而在此創造出的虛擬世界中有你我的數位分身，以及相關的權利與資產，要保障這些安全，區塊鏈成為虛擬世界的私人鑰匙，元宇宙的世界必須建立在其基礎上，在元宇宙中結合了AI、AR和VR，而這一切也需要5G的高速傳輸協助。</p><!--10--><p>
 </p><p>
光通訊產品分成主動及被動元件，主動元件負責光訊號的產生及接收，被動元件則是負責光訊號的傳遞與調變，光環為主動元件廠，多數網通廠多擁有「三年不開張，開張吃三年」的特色，每次歷經通訊技術的換代，都會為營運帶來好光景，2015大賺 8.04元，股價當時最高衝到120元，目前雖然營運尚未好轉，不過在第四季走題材行情下，有望籍「馬斯克熱潮」吸引市場注意。</p><!--11--><p>
 </p><p>
本公司與所推介分析之個別有價證券</p><p>
無不當之財務利益關係 以往之績效不保證未來獲利</p><!--12--><p>
投資人應獨立判斷  審慎評估並自負投資風險</p><!--13--><p>
</p><p>
</p><!--99-->                      <div>
	    <br>
<br>
<font size="3">※ 歡迎用「轉貼」或「分享」的方式轉傳文章連結；未經授權，請勿複製轉貼文章內容</font><br>
<br></div>
<div>
	    <center><a href="https://money.udn.com/ACT/2021/industrystrategy/index.html"><img src="https://money.udn.com/SSI/ednvip/banner/vip_article_end_banner_20211102.jpg"></a></center></div>
<div>
	<script>
var mobileOrDesktop = ($(window).width() < 768) ?　'mobile' : 'desktop';
var stockAction = '';
var searchStockNumber = function () {
            var re = /（(?:\d){4,5}）/g;
            const filterTxt = ['明年', '後年', '前年', '去年', '今年', '今', '前', '明', '年'];
            var totalCheckItem = [];
            var articleContent = document.getElementById('article_body').innerHTML;
            var totalStocknumber = [];
            var indexArray = [0];
            var ary;

        while((ary = re.exec(articleContent)) !== null) {
            var totalNumber = ary[0]
            if(filterTxt.indexOf(ary.input.substr(ary.index-2, 2)) > -1 || (filterTxt.indexOf(ary.input.substr(ary.index-1, 1))> -1 && ary.input.substr(ary.index + ary[0].length, 1).indexOf('年') > -1)){

            }else {
                totalCheckItem.push(ary)
                totalStocknumber.push(ary[0].substr(1, ary[0].length - 2))
            }
            // 符合以上條件的排除
        }

    var indexs = 0;
            for (var i = 0; i < totalCheckItem.length - 1; i++) {
                indexs += totalCheckItem[i][0].length - 1
                indexArray.push(indexs)
                // console.log(indexArray)
            };
            var strArr = articleContent.split('');
            for (var i = 0, j = 0; i < totalCheckItem.length; i++) {
                strArr.splice(totalCheckItem[i].index - indexArray[i], totalCheckItem[i][0].length, '<a class="systex-link" target="_blank" href="https://money.udn.com/common/systex_login/' + mobileOrDesktop + '/' + totalStocknumber[i] + '">' + totalCheckItem[i][0] + '</a>')
            };
            strArr = strArr.join('');
            $('#article_body').html(strArr);

// 若有搜尋到股號，在文章結尾插入iframe以及看更多按鈕     
            if (totalStocknumber.length > 0) {
                $('#article_body').append('<div class="stock_more_button"><a class="stockmoreLab" href="https://money.udn.com/common/systex_login/'+
                      mobileOrDesktop + '/' + totalStocknumber[0] + '?pure=n" target="_blank" id="stockmore_button">前往看盤</a></div>')

                    $('#article_body .stock_more_button').append('<a class="stockmoreLab stockorder" href="#"  id="stockorder_button" onclick="openSPWin(\'https://www.sinotrade.com.tw/newweb/OrderGO/?platform=udn&type=S&stockid=' + totalStocknumber[0] +'&utm_campaign=NW_TSP_02&utm_source=udn&utm_medium=button_0601&strProd=0102&strWeb=0135\');return false;">個股下單</a>')    

                $('#article_body').append('<iframe id="stock_iframe" src="https://pelements.money-link.com.tw/B2B/twstock/TAprice.html?symid=' + totalStocknumber[0] + '"' + 'allowTransparency="true" marginwidth="0" marginheight="0" scrolling="No" frameborder="0" style="width:100%;"></iframe>')
            }else{
                $('#article_body').append('<div class="stock_more_button"><a class="stockmoreLab" style = display:none; ></a></div>')
                $('#article_body .stock_more_button').append('<a class="stockmoreLab stockorder" href="#" style = display:none;></a>')    
            }
        };
var openSPWin = function(url){
		var sinoPacWO = window.open("about：blank","永豐金",config="width=500,height=700");
		setSPlink(url)
	};
var setSPlink = function(url) {
		 sinoPacWO = window.open(url,"永豐金",config="width=500,height=700");
	};

var GetCkValue = function( name ) {
    var dc=document.cookie;
    var prefix=name+"=";
    var begin=dc.indexOf("; "+prefix);
    if(begin==-1) begin=dc.indexOf(prefix);
    else begin+=2;
    if(begin==-1) return "";
    var end=document.cookie.indexOf(";",begin);
    if(end==-1) end=dc.length;
    return dc.substring(begin+prefix.length,end);
}
var checkmember = function() {
    // alert($(this).prop("href")); // return false;
    if($(this).attr('class') == 'systex-link'){
        stockAction = '?site=money&event=systex_stock';
   }else{
       stockAction = '?site=money&event=systex_market';
   }
    var data = {
        udnmember: GetCkValue("udnmember"),
        um2: GetCkValue("um2"),
        udngold: GetCkValue("udngold"),
        udnland: GetCkValue("udnland"),
        services: GetCkValue("services"),
        art_id: rId(),
        sub_id: scId()
    };
    var systexurl = $(this).prop("href");
    $.ajax({
        type: 'GET',
        url: '/money/ajax_check_member',
        data: data,
        dataType: 'json',
        success: function (response) {
            if(response.status) {
                // ok 直接過去
                // window.open(systexurl, '_blank');
                $('#article_body').append('<a id="proxyUrl" target="_blank" href="'+systexurl+'"></a>');
                $("#proxyUrl")[0].click();
                $("#proxyUrl").remove();
            } else {
                if(response.service == 1) {
                    // 啟用會員閱讀全文
                    openmoney();
                } else {
                    // 請登入閱讀全文
                    $.confirm({
                        title: '',
                        content: '請登入會員，立刻享受即時股市看盤服務',
                        boxWidth: '285px',
                        useBootstrap: false,
                        buttons: {
                            confirm: {
                                btnClass: 'btn-default stock-login',
                                text: '登入',
                                action: function () {
                                    // ga('create', 'UA-19210365-3', 'auto', {'name': 'money'});
                                    // ga('send', 'event', 'article', 'click', '登入閱讀全文');
                                    window.location.href='https://money.udn.com/member/member_login?site=money&again=y&clickcta=subscribe&redirect='+$('meta[property="og:url"]').attr('content') + stockAction ;
                                }
                            },
                            cancel: {
                                btnClass: 'btn-default stock-login-wait',
                                text: '稍後再說',
                                action: function () {}
                            }
                        }
                    });
                }
            }
        }
    });
    return false;
};
var openmoney = function() {
    $.confirm({
        title: '',
        content: '立即啟用，享受經濟日報會員全服務',
        boxWidth: '285px',
        useBootstrap: false,
        buttons: {
            confirm: {
                btnClass: 'btn-default stock-action',
                text: '啟用',
                action: function () {
                    $.ajax({
                        type : 'POST',
                        url : '/api/v1/member/activeMoneyMember' + stockAction ,
                        async:false,
                        xhrFields: {withCredentials: true},
                        crossDomain:true,
                        success : function (response){
                            if(response['success'] == true) {
                                alert('啟用成功');
                                // window.open(`https://money.udn.com/common/systex_login/${mobileOrDesktop}/?pure=n`);
                                // var systexurl = `https://money.udn.com/common/systex_login/${mobileOrDesktop}/?pure=n`;
                                var systexurl = 'https://money.udn.com/common/systex_login/'+ mobileOrDesktop + '/?pure=n';
                                $('#article_body').append('<a id="proxyUrl" target="_blank" href="'+systexurl+'"></a>');
                                $("#proxyUrl")[0].click();
                                $("#proxyUrl").remove();
                            } else {
                                alert('啟用失敗，請洽管理人員');
                                console.log('activeMoneyMember: fail');
                            }
                        },
                        error : function(){
                            alert('啟用失敗，請洽管理人員');
                            console.log('activeMoneyMember: error');
                        }
                    }); // end
                }
            },
            cancel: {
                btnClass: 'btn-default stock-action-wait',
                text: '稍後再說',
                action: function () {}
            }
        }
    });
};

$(document).ready(function () {
    console.log($('#article_body .stock_more_button').length)
    if( $('#article_body .stock_more_button').length <= 0 ){
        searchStockNumber();
    }
  $("a.stockmore").off('click').on('click', checkmember);
  $("a.systex-link").off('click').on('click', checkmember);
});
</script>

<style>
.stock_more_button {
  position: relative;
  text-align:right;
  margin-top: 26px;
}
#stock_iframe {
  height:400px;
  margin-bottom:10px;
}
.stockmoreLab {
  margin-bottom: -20px;
  font-size: 14px;
  padding: 0 8.7px;
  cursor: pointer;
  background-color: #EBEBEB;
  color: #E50027 !important;
  border-radius: 15px;
  display: inline-block;
  line-height: 25px;
  font-weight: bold;
  letter-spacing: 0px;
}

.stockmore {
text-align:right;
padding:10px;
cursor: pointer;
background-color: #e50027;
color: #fff!important;
font-size:14px;
border-radius:5px;
display:inline-block;
}

.stockorder {
margin-left: 5px
}

.stockmore:hover,.stockmoreLab:hover {
text-decoration: none!important;
}
.box{
margin: 10px auto 30px!important;
}

@media screen and (max-width:767px) {
#stock_iframe {
  height:460px;

}

}
</style>
</div>
                  <div class="stock_more_button"><a class="stockmoreLab" style="display:none;"></a><a class="stockmoreLab stockorder" href="#" style="display:none;"></a></div></section>

                                  </section>
              </article>
              	<section class="article-keyword">
	<ul class="article-keyword__list">
					<li class="article-keyword__item">
		<a href="/search/tagging/1001/馬斯克" rel="145331">馬斯克</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/半導體" rel="94683">半導體</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/惠宇" rel="152325">惠宇</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/磊晶片" rel="95770">磊晶片</a>
		</li>
				<li class="article-keyword__item">
		<a href="/search/tagging/1001/元宇宙" rel="176948">元宇宙</a>
		</li>
			</ul>
</section>
<!-- Loction：temp_new/inc/content/story/article_tag -->                <section class="social-bar">
                  <ul class="social-bar__list">
                    <li class="social-bar__item">
                      <a href="#" class="fb">
                        <i class="i-facebook-1"></i>
                      </a>
                    </li>
                    <li class="social-bar__item">
                      <a href="#" class="line">
                        <i class="i-line"></i>
                      </a>
                    </li>
                    <li class="social-bar__item">
                      <a href="#" class="bookmark">
                        <i class="i-bookmark"></i>
                      </a>
                    </li>
                    <li class="social-bar__item">
                      <a href="#" class="fontsize">
                        <i class="i-text-size"></i>
                      </a>
                    </li>
                    <li class="social-bar__item">
                      <a href="#" class="msg">
                        <i class="i-talk"></i>
                      </a>
                    </li>
                  </ul>
                </section>
                              <section class="article-columnist columnist-profile">
                  <div class="image-text-wrapper">
                    <div class="columnist-profile__image">
                                              <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/author/photo/2502.jpg&amp;x=&amp;y=&amp;sw=&amp;sh=&amp;exp=3600&amp;20211102cleancache&amp;sl=H&amp;fh=120" height="120">
                                          </div>
                    <div class="pad-show--inline-block">
                        <h3 class="columnist-profile__name"><a href="/author/articles/2502">萬寶週刊</a></h3>
                    </div>
                  </div>
                  <div class="columnist-profile__content">
                    <div class="web-only">
                        <h3 class="columnist-profile__name"><a href="/author/articles/2502">萬寶週刊</a></h3>
                    </div>
                    <p class="columnist-profile__text">
                        《萬寶週刊》鎖定中高資產族群，以台股、全球股市、期貨、基金、房地產、藝術、精品投資為主軸，出版至今深受投資界人士青睞，為全國證券界指標性刊物。每週由記者群及研究小組，挖掘不為人知的第一手消息，放眼全球投資。                    </p>
                  </div>
                </section>
                <!-- .article-columnist -->
                                <section class="edn-ads--text">
                    <!-- H／B版本 -->
<!-- /129853887/udn.com/money/Web/money-PcMobile-endtxt 【經濟VIP】內文文末文字廣告 -->
<style>
.edn-ads--text > div {
    width:100%;
}
</style>
<div id="div-gpt-ad-1564727433317-0">
<script>
googletag.cmd.push(function() {
 var sizeMapping = googletag.sizeMapping().
            addSize([750, 200], ['fluid']).
            addSize([0, 0], ['fluid']).
            build()

 googletag.defineSlot('/129853887/udn.com/money/Web/money-PcMobile-endtxt', ['fluid'], 'div-gpt-ad-1564727433317-0')
   .defineSizeMapping(sizeMapping)
   .addService(googletag.pubads());

 googletag.display('div-gpt-ad-1564727433317-0');
});
</script>
</div>                </section>
                                  <section class="article-extend">
                  <h3>延伸閱讀</h3>
                    <ul class="story-flex-bt-wrapper">
                                                  <li class="story-headline-wrapper story">
                            <div class="story__image">
                              <a href="https://money.udn.com/money/story/5612/5856974?from=edn_referralnews_story_ch5590">
                                <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/10/31/2/14452204.jpg&amp;s=Y&amp;x=0&amp;y=0&amp;sw=720&amp;sh=480&amp;sl=W&amp;fw=640" alt="news photo">
                              </a>
                            </div>
                                                          <div class="story__content story__content--key">
                                                          <a href="https://money.udn.com/money/story/5612/5856974?from=edn_referralnews_story_ch5590">
                              <h3 class="story__headline">
                                元晶結緣馬斯克 從地表做到外太空                              </h3>
                                                              <time>10/31 21:21</time>
                                                            </a>
                            </div>
                          </li>
                                                  <li class="story-headline-wrapper story">
                            <div class="story__image">
                              <a href="https://money.udn.com/money/story/5607/5851330?from=edn_referralnews_story_ch5590">
                                <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/10/29/realtime/14430944.jpg&amp;s=Y&amp;x=0&amp;y=0&amp;sw=1279&amp;sh=853&amp;sl=W&amp;fw=640" alt="news photo">
                              </a>
                            </div>
                                                          <div class="story__content">
                                                          <a href="https://money.udn.com/money/story/5607/5851330?from=edn_referralnews_story_ch5590">
                              <h3 class="story__headline">
                                馬斯克登首富預告新主流！「通吃」特斯拉和鴻海，兩岸零組件廠大盤點                              </h3>
                                                              <time>10/29 00:14</time>
                                                            </a>
                            </div>
                          </li>
                                                  <li class="story-headline-wrapper story">
                            <div class="story__image">
                              <a href="https://money.udn.com/money/story/5607/5848146?from=edn_referralnews_story_ch5590">
                                <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/10/27/realtime/14417452.jpg&amp;s=Y&amp;x=0&amp;y=9&amp;sw=1280&amp;sh=852&amp;sl=W&amp;fw=640" alt="news photo">
                              </a>
                            </div>
                                                          <div class="story__content">
                                                          <a href="https://money.udn.com/money/story/5607/5848146?from=edn_referralnews_story_ch5590">
                              <h3 class="story__headline">
                                《大賣空》本尊放棄看空特斯拉！低軌道衛星商機，台廠四大零組件誰最有看頭？                              </h3>
                                                              <time>10/27 22:17</time>
                                                            </a>
                            </div>
                          </li>
                                                  <li class="story-headline-wrapper story">
                            <div class="story__image">
                              <a href="https://money.udn.com/money/story/5607/5845730?from=edn_referralnews_story_ch5590">
                                <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/10/07/2/14200711.png&amp;s=Y&amp;x=135&amp;y=0&amp;sw=545&amp;sh=363&amp;sl=W&amp;fw=640" alt="news photo">
                              </a>
                            </div>
                                                          <div class="story__content">
                                                          <a href="https://money.udn.com/money/story/5607/5845730?from=edn_referralnews_story_ch5590">
                              <h3 class="story__headline">
                                明年台股不是誰都漲！綠能、車電、元宇宙等族群，誰的實力比較強？                              </h3>
                                                              <time>10/27 00:06</time>
                                                            </a>
                            </div>
                          </li>
                                                  <li class="story-headline-wrapper story">
                            <div class="story__image">
                              <a href="https://money.udn.com/money/story/5599/5843288?from=edn_referralnews_story_ch5590">
                                <img src="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/10/26/realtime/14408201.jpeg&amp;s=Y&amp;x=0&amp;y=0&amp;sw=1280&amp;sh=853&amp;sl=W&amp;fw=640" alt="news photo">
                              </a>
                            </div>
                                                          <div class="story__content">
                                                          <a href="https://money.udn.com/money/story/5599/5843288?from=edn_referralnews_story_ch5590">
                              <h3 class="story__headline">
                                史上最大綠能車訂單推升特斯拉市值破1兆美元 馬斯克進財                              </h3>
                                                              <time>10/26 08:05</time>
                                                            </a>
                            </div>
                          </li>
                                            </ul>
                  </section>
                                                <section class="article-switch">
                  <div class="article-switch__prev">

                    <a href="/money/story/5607/5859986?from=edn_previous_story" class="article-switch__btn">上一篇</a>
                                          <div class="story__content">
                                          <a href="/money/story/5607/5859986?from=edn_previous_story" class="story__headline">
                        11月2日重要財經行事曆                      </a>
                    </div>
                                      </div>
                  <div class="article-switch__next">
                                      <a href="/money/story/5607/5859422?from=edn_next_story" class="article-switch__btn">下一篇</a>
                                          <div class="story__content">
                                          <a href="/money/story/5607/5859422?from=edn_next_story" class="story__headline">
                        元宇宙沒那麼快漲完  「隱藏版」概念股還有誰？                      </a>
                    </div>
                                      </div>
                </section>
              <div class="edn-ads--pad">
                <!--
<a href="https://www.books.com.tw/products/0010873471?sloc=main" target="_blank">
   <img src="https://uc.udn.com.tw/upf/2015_money/SSI/ad/202010281_ad.jpg" width="300" height="225" alt="股債雙存獲利六堂課" title="股債雙存獲利六堂課">
</a>
-->

<!-- /129853887/udn.com/2_money/3_money-Mobile/4_money-Mobile-a01 經濟VIP Mobile第二大佈告 -->
<div id="google_ad">
<div id="div-gpt-ad-1633326636560-0" style="margin:0px auto;">
  <script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-1633326636560-0'); });
  </script>
</div>
</div>              </div>
              <div class="story-flex-bt-wrapper">
              <section class="article-related story">
                    <h3>相關</h3>
                    <ul class="article__list">
                                                                                                                                                                              <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5861657?from=edn_related_storybottom">電子遇亂流！獲利了結賣壓重 台股多空交戰守季線</a>
                                </li>
                                                                                                                            <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5861376?from=edn_related_storybottom">環球晶前三每股純益22.4元 業績看旺</a>
                                </li>
                                                                                                                            <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5861241?from=edn_related_storybottom">元宇宙拉回台股收跌2.27點 三大法人賣超2.31億</a>
                                </li>
                                                                                                                            <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5860927?from=edn_related_storybottom">台股下跌2點收17,065點 元宇宙及車電漲多拉回</a>
                                </li>
                                                                                                                            <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5860585?from=edn_related_storybottom">台股解盤/元宇宙、低軌衛星還可不可以買? 法人這麼看</a>
                                </li>
                                                                                                                            <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5860243?from=edn_related_storybottom">櫃買領先創逾二個月新高 分析師：已連漲13天要小心</a>
                                </li>
                                                                                                                            <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5860047?from=edn_related_storybottom">台股早盤漲逾百點 台積電開盤上漲4元</a>
                                </li>
                                                                                                                            <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5859726?from=edn_related_storybottom">台股收復萬七 櫃買連13紅</a>
                                </li>
                                                                                                                            <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5860178?from=edn_related_storybottom">和碩左攻墨西哥右打元宇宙 早盤股價近4個月新高</a>
                                </li>
                                                                                                                            <li class="article__item more2 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5859308?from=edn_related_storybottom">伺服器鏈 短多點火</a>
                                </li>
                                                                                                                            <li class="article__item more3 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5861939?from=edn_related_storybottom">今日最夯股/歐買尬轉投資綠界科技 母憑子貴價量齊揚 </a>
                                </li>
                                                                                                                            <li class="article__item more3 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5861975?from=edn_related_storybottom">今日最夯股/聯華本業表現出色 搶攻減碳商機</a>
                                </li>
                                                                                                                            <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5607/5859887?from=edn_related_storybottom">11月2日 五件財經大事搶先看</a>
                                </li>
                                                                                                                            <li class="article__item more3 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5861979?from=edn_related_storybottom">台股擂台/「股市航海王」何基鼎：中小型類股走勢強於大盤，可留意電動車相關電子族群</a>
                                </li>
                                                                                                                            <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5607/5861480?from=edn_related_storybottom">元宇宙概念發酵 投信聚焦顛覆式創新投資機會</a>
                                </li>
                                                                                                                            <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5861227?from=edn_related_storybottom">三大法人賣超台股2.31億元</a>
                                </li>
                                                                                                                            <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5861163?from=edn_related_storybottom">台股開高走低 法人盤點Q4主流類股</a>
                                </li>
                                                                                                                            <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5861030?from=edn_related_storybottom">中小型股中箭落馬  台股開高走低力守萬七大關</a>
                                </li>
                                                                                                                            <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5860973?from=edn_related_storybottom">台股開高走低 收跌2.27點</a>
                                </li>
                                                                                                                            <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5860205?from=edn_related_storybottom">凱基投顧看好三利多 台股迎財報上修行情</a>
                                </li>
                                                                                                                            <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860134?from=edn_related_storybottom">權值股回神 台股上漲逾百點攻克半年線</a>
                                </li>
                                                                                                                            <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860053?from=edn_related_storybottom">台股開盤漲26.18點</a>
                                </li>
                                                                                                                            <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860027?from=edn_related_storybottom">台指期開盤上漲87點 台積期貨開盤上漲2元</a>
                                </li>
                                                                                                                            <li class="article__item more5 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5860013?from=edn_related_storybottom">盤前分析/台股短線技術面持續偏多 有利中小型股</a>
                                </li>
                                                                                                                            <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860002?from=edn_related_storybottom">今日台股盤前重點掃描</a>
                                </li>
                                                                                                                            <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5859996?from=edn_related_storybottom">美股再創高 台股待長紅突破盤局</a>
                                </li>
                                                                                                                            <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5859986?from=edn_related_storybottom">11月2日重要財經行事曆</a>
                                </li>
                                                                                                                            <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5859426?from=edn_related_storybottom">一覺醒來資產多1兆！馬斯克登首富宣告三主流，電動車、低軌衛星、元宇宙明年誰成真？</a>
                                </li>
                                                                                                                            <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5859422?from=edn_related_storybottom">元宇宙沒那麼快漲完  「隱藏版」概念股還有誰？</a>
                                </li>
                                                                                                                            <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5859443?from=edn_related_storybottom">面板、貨櫃難逃週期股宿命？他以NVIDIA市值超過台積為例：選股邏輯正在改變</a>
                                </li>
                                                                                                                            <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5607/5859715?from=edn_related_storybottom">宇宙人將原形畢露？資深投資人：靠著空單軋上去  接下來輪到多軍做惡夢</a>
                                </li>
                                                                                                                            <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5607/5859304?from=edn_related_storybottom">環宇周五法說 聚焦5G基建</a>
                                </li>
                                                                                                                            <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5607/5859305?from=edn_related_storybottom">就市論勢/IC設計、電子紙 可留意</a>
                                </li>
                                                                                                                            <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5607/5859170?from=edn_related_storybottom">ABF三雄 高盛升目標價</a>
                                </li>
                                                                                                                            <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5607/5859309?from=edn_related_storybottom">富邦基因免疫ETF題材熱</a>
                                </li>
                                                                                                                            <li class="article__item more8 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5859400?from=edn_related_storybottom">今日最夯股/ 搶搭自駕車 大億金茂量增漲停</a>
                                </li>
                                                                                                                            <li class="article__item more8 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5859389?from=edn_related_storybottom">今日最夯股/ 太陽能還會漲價  聯合再生攻漲停</a>
                                </li>
                                                                                                                            <li class="article__item more8 article__item--key" style="display:none;">
                                                                  <a href="/money/story/5607/5859284?from=edn_related_storybottom">台股擂台/「趨勢判官」田大為：台股震盪整理 操作不追高</a>
                                </li>
                                                                                                                            <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5607/5858868?from=edn_related_storybottom">抗通膨資產股  上市櫃建商全台購地「前五名」揭曉</a>
                                </li>
                                                                                                                            <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5607/5858864?from=edn_related_storybottom">一路缺貨到2023年  ABF載板還有大行情嗎？</a>
                                </li>
                                                                      </ul>
                  </section>
                  <section class="article-hot story">
                    <h3>熱門</h3>
                    <ul class="article__list">
                                                                                                                                                                          <li class="article__item more1" style="">
                                                                  <a href="/money/story/5710/5860066?from=edn_hotestlist_storybottom">宇宙人營運結果出來了！宏達電Q3每股虧損0.94元 股價不受影響續漲</a>
                              </li>
                                                                                                                        <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5860585?from=edn_hotestlist_storybottom">台股解盤/元宇宙、低軌衛星還可不可以買? 法人這麼看</a>
                              </li>
                                                                                                                        <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5859887?from=edn_hotestlist_storybottom">11月2日 五件財經大事搶先看</a>
                              </li>
                                                                                                                        <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5859726?from=edn_hotestlist_storybottom">台股收復萬七 櫃買連13紅</a>
                              </li>
                                                                                                                        <li class="article__item more1" style="">
                                                                  <a href="/money/story/5607/5860178?from=edn_hotestlist_storybottom">和碩左攻墨西哥右打元宇宙 早盤股價近4個月新高</a>
                              </li>
                                                                                                                        <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5861241?from=edn_hotestlist_storybottom">元宇宙拉回台股收跌2.27點 三大法人賣超2.31億</a>
                              </li>
                                                                                                                        <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5860927?from=edn_hotestlist_storybottom">台股下跌2點收17,065點 元宇宙及車電漲多拉回</a>
                              </li>
                                                                                                                        <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5860243?from=edn_hotestlist_storybottom">櫃買領先創逾二個月新高 分析師：已連漲13天要小心</a>
                              </li>
                                                                                                                        <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5607/5861657?from=edn_hotestlist_storybottom">電子遇亂流！獲利了結賣壓重 台股多空交戰守季線</a>
                              </li>
                                                                                                                        <li class="article__item more2" style="display:none;">
                                                                  <a href="/money/story/5710/5859971?from=edn_hotestlist_storybottom">宏達電2021年前三季 每股虧損2.86元</a>
                              </li>
                                                                                                                        <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5607/5860047?from=edn_hotestlist_storybottom">台股早盤漲逾百點 台積電開盤上漲4元</a>
                              </li>
                                                                                                                        <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5710/5861787?from=edn_hotestlist_storybottom">華新科第3季獲利、EPS 均寫近11季來高點</a>
                              </li>
                                                                                                                        <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5710/5861646?from=edn_hotestlist_storybottom">環球晶前三季每股純益22.4元 今年仍有望賺進三個股本</a>
                              </li>
                                                                                                                        <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5607/5859986?from=edn_hotestlist_storybottom">11月2日重要財經行事曆</a>
                              </li>
                                                                                                                        <li class="article__item more3" style="display:none;">
                                                                  <a href="/money/story/5710/5859984?from=edn_hotestlist_storybottom">世界2021年前三季 每股獲利4.94元</a>
                              </li>
                                                                                                                        <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5710/5860280?from=edn_hotestlist_storybottom">宏達電Q3每股虧0.94元 毛利率勁揚至31.6%</a>
                              </li>
                                                                                                                        <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5860002?from=edn_hotestlist_storybottom">今日台股盤前重點掃描</a>
                              </li>
                                                                                                                        <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5860205?from=edn_hotestlist_storybottom">凱基投顧看好三利多 台股迎財報上修行情</a>
                              </li>
                                                                                                                        <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5710/5861678?from=edn_hotestlist_storybottom">台灣櫻花前三季每股3.31元創同期新高 Q4衝五倍券商機</a>
                              </li>
                                                                                                                        <li class="article__item more4" style="display:none;">
                                                                  <a href="/money/story/5607/5861975?from=edn_hotestlist_storybottom">今日最夯股/聯華本業表現出色 搶攻減碳商機</a>
                              </li>
                                                                                                                        <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/11074/5860008?from=edn_hotestlist_storybottom">台慶科11月2日起 得為融資融券交易</a>
                              </li>
                                                                                                                        <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5861979?from=edn_hotestlist_storybottom">台股擂台/「股市航海王」何基鼎：中小型類股走勢強於大盤，可留意電動車相關電子族群</a>
                              </li>
                                                                                                                        <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860027?from=edn_hotestlist_storybottom">台指期開盤上漲87點 台積期貨開盤上漲2元</a>
                              </li>
                                                                                                                        <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5607/5860013?from=edn_hotestlist_storybottom">盤前分析/台股短線技術面持續偏多 有利中小型股</a>
                              </li>
                                                                                                                        <li class="article__item more5" style="display:none;">
                                                                  <a href="/money/story/5710/5861923?from=edn_hotestlist_storybottom">京元電2.89元 本季衝高</a>
                              </li>
                                                                                                                        <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5710/5861922?from=edn_hotestlist_storybottom">華新科前三季EPS 14.4元</a>
                              </li>
                                                                                                                        <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5739/5862275?from=edn_hotestlist_storybottom">鴻海動能強 鎖定價平</a>
                              </li>
                                                                                                                        <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5607/5861939?from=edn_hotestlist_storybottom">今日最夯股/歐買尬轉投資綠界科技 母憑子貴價量齊揚 </a>
                              </li>
                                                                                                                        <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/8044/5851522?from=edn_hotestlist_storybottom">1102 指標焦點股</a>
                              </li>
                                                                                                                        <li class="article__item more6" style="display:none;">
                                                                  <a href="/money/story/5739/5862271?from=edn_hotestlist_storybottom">和大、中橡 四檔馬力強</a>
                              </li>
                                                                                                                        <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5710/5862033?from=edn_hotestlist_storybottom">融程電Q3獲利創新高</a>
                              </li>
                                                                                                                        <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/9607/5851510?from=edn_hotestlist_storybottom">1102 國內共同基金淨值</a>
                              </li>
                                                                                                                        <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/11074/5861892?from=edn_hotestlist_storybottom">環球晶前三季EPS 22.4元</a>
                              </li>
                                                                                                                        <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/5739/5862259?from=edn_hotestlist_storybottom">瑞昱 優選逾90天</a>
                              </li>
                                                                                                                        <li class="article__item more7" style="display:none;">
                                                                  <a href="/money/story/11074/5861999?from=edn_hotestlist_storybottom">大田前三季獲利登峰</a>
                              </li>
                                                                                                                        <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5710/5861871?from=edn_hotestlist_storybottom">遠東新拚再生聚酯龍頭</a>
                              </li>
                                                                                                                        <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/9625/5851515?from=edn_hotestlist_storybottom">1102 上市櫃公司熱門股排行</a>
                              </li>
                                                                                                                        <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5739/5862260?from=edn_hotestlist_storybottom">南電 二檔強強滾</a>
                              </li>
                                                                                                                        <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5739/5862269?from=edn_hotestlist_storybottom">聯發科凌陽認購夯</a>
                              </li>
                                                                                                                        <li class="article__item more8" style="display:none;">
                                                                  <a href="/money/story/5739/5862255?from=edn_hotestlist_storybottom">台光電 押價外15%</a>
                              </li>
                                                                      </ul>
                  </section>
                  <a href="#" class="story__read-more story__read-more--related" data-page="1">
                    <h3>看更多</h3>
                    <i class="i-arrow5-down"></i>
                  </a>
                  <a href="#" class="story__read-more story__read-more--hot" data-page="1">
                    <h3>看更多</h3>
                    <i class="i-arrow5-down"></i>
                  </a>
              </div>
              <section class="article-also-like">
                                                          <!--div id="member_only">開放閱讀</div-->
                                            <div id="_popIn_recommend"><div class="_popIn_recommend_container" data-channel-id="with_sz_all_ltr__pc_new_ui_addOneAd" id="popIn_recommend_with_img"><div class="_popIn_recommend_header">您可能也喜歡</div><div class="_popIn_recommend_articles"><div class="_popIn_infinite_page"><div class="_popIn_recommend_article _popIn_idx1 _popIn_recommend_article_ad _popIn_recommend_has_img _popIn_recommend_img_fit"><div class="_popIn_recommend_art_img"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.bosch-home.com.tw%2Fspecials%2F90days%3Fcid%3D90days~disp~~~popin~~~bnr~~%26tripid%3D7e810f940326fbe31ed2f1344d15b172%26popintoken%3D7e810f940326fbe31ed2f1344d15b172%26ad_click_time%3D1635871762558%26rdt%3D1&amp;data=eyJjdmlkIjoiYWRHX2Jvc2NoMDUiLCJjIjoiMy4wIiwidHoiOiJ0dyIsImYiOiIyIiwibmlkIjoiNjE1MTkxZjdmNjg2YjY2NmJhNzU3Mzk1IiwibV9jYXQiOiIiLCJjYW1wYWlnbiI6IjYxNTE5MWNjZjY4NmI2NzliYjU3YzgwNCIsIm1lZGlhIjoibW9uZXkudWRuLmNvbSIsImNhdGVnb3J5IjoiYnVzaW5lc3MiLCJtIjoiMjcyNjQ1MjkiLCJkZXZpY2UiOiJwYyIsImxfY2F0IjoiSUFCMjYifQ==&amp;token=7e810f940326fbe31ed2f1344d15b172&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/discovery/1bf496fa26378fd09666a6a8900024ef.jpeg&quot;); background-size: contain; background-repeat: no-repeat;"></a></div><div class="_popIn_recommend_art_title"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.bosch-home.com.tw%2Fspecials%2F90days%3Fcid%3D90days~disp~~~popin~~~bnr~~%26tripid%3D7e810f940326fbe31ed2f1344d15b172%26popintoken%3D7e810f940326fbe31ed2f1344d15b172%26ad_click_time%3D1635871762559%26rdt%3D1&amp;data=eyJjdmlkIjoiYWRHX2Jvc2NoMDUiLCJjIjoiMy4wIiwidHoiOiJ0dyIsImYiOiIyIiwibmlkIjoiNjE1MTkxZjdmNjg2YjY2NmJhNzU3Mzk1IiwibV9jYXQiOiIiLCJjYW1wYWlnbiI6IjYxNTE5MWNjZjY4NmI2NzliYjU3YzgwNCIsIm1lZGlhIjoibW9uZXkudWRuLmNvbSIsImNhdGVnb3J5IjoiYnVzaW5lc3MiLCJtIjoiMjcyNjQ1MjkiLCJkZXZpY2UiOiJwYyIsImxfY2F0IjoiSUFCMjYifQ==&amp;token=7e810f940326fbe31ed2f1344d15b172&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow">另一半的手是用來牽的 ! 解放洗碗的粗糙手，婚姻幸福就靠Bosch洗碗機神隊友 !</a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_media">PR</div><div class="_popIn_recommend_art_date"></div></div><div class="_popIn_recommend_article _popIn_idx2 _popIn_recommend_article_cf _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://money.udn.com/money/story/5612/5850409?from=popinpc2" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/article/9b80ac2dbfab638de5fcd797a803099a_160.jpg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://money.udn.com/money/story/5612/5850409?from=popinpc2">全聯才吞下大潤發 林敏雄下個戰場提前曝光 </a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_date">(2021年10月28日)</div></div><div class="_popIn_recommend_article _popIn_idx3 _popIn_recommend_article_ad _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.ystore.com.tw%2Fevents%2Fmadesking%3Futm_source%3DpopIn%26utm_medium%3Dcpc%26utm_campaign%3D0426%26tripid%3D81a5957293ff548b2a2d5c21fa392511%26popintoken%3D81a5957293ff548b2a2d5c21fa392511%26ad_click_time%3D1635871762559%26rdt%3D1&amp;data=eyJjdmlkIjoieWFobyIsImMiOiIzLjAiLCJ0eiI6InR3IiwiZiI6IjIiLCJuaWQiOiI2MTVlYzQxMmY2ODZiNjI4YzQ3NjBmMzQiLCJtX2NhdCI6IiIsImNhbXBhaWduIjoiNjAxOGYyYTAwZmMxMGMxYjBmMTBlYzQ0IiwibWVkaWEiOiJtb25leS51ZG4uY29tIiwiY2F0ZWdvcnkiOiJidXNpbmVzcyIsIm0iOiIyNzI2NDUyOSIsImRldmljZSI6InBjIiwibF9jYXQiOiJJQUIxMiJ9&amp;token=81a5957293ff548b2a2d5c21fa392511&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/discovery/06c3f9694b4ae03365504a78014935b0.jpeg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.ystore.com.tw%2Fevents%2Fmadesking%3Futm_source%3DpopIn%26utm_medium%3Dcpc%26utm_campaign%3D0426%26tripid%3D81a5957293ff548b2a2d5c21fa392511%26popintoken%3D81a5957293ff548b2a2d5c21fa392511%26ad_click_time%3D1635871762565%26rdt%3D1&amp;data=eyJjdmlkIjoieWFobyIsImMiOiIzLjAiLCJ0eiI6InR3IiwiZiI6IjIiLCJuaWQiOiI2MTVlYzQxMmY2ODZiNjI4YzQ3NjBmMzQiLCJtX2NhdCI6IiIsImNhbXBhaWduIjoiNjAxOGYyYTAwZmMxMGMxYjBmMTBlYzQ0IiwibWVkaWEiOiJtb25leS51ZG4uY29tIiwiY2F0ZWdvcnkiOiJidXNpbmVzcyIsIm0iOiIyNzI2NDUyOSIsImRldmljZSI6InBjIiwibF9jYXQiOiJJQUIxMiJ9&amp;token=81a5957293ff548b2a2d5c21fa392511&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow">呆板辦公桌做事好不順心？這款動態升降桌，讓工作狂熱者愛不釋手！</a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_media">PR</div><div class="_popIn_recommend_art_date"></div></div><div class="_popIn_recommend_article _popIn_idx4 _popIn_recommend_article_hot _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://money.udn.com/money/story/5607/5858864?from=popinpc2" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/article/6a22e69c1ceba57c2c6b501d2ca4ad7c_160.jpg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://money.udn.com/money/story/5607/5858864?from=popinpc2">一路缺貨到2023年 ABF載板還有大行情嗎？ </a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_date">(2021年11月1日)</div></div></div><div class="_popIn_infinite_page"><div class="_popIn_recommend_article _popIn_idx1 _popIn_recommend_article_cf _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://money.udn.com/money/story/12040/5845858?from=popinpc2" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/article/013de0953c1c4ff240792e0d4381aebc_160.jpg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://money.udn.com/money/story/12040/5845858?from=popinpc2">主力大戶也被割韭菜？台股老手示警：航海王、東森之後 接下來小心「宇宙人」 </a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_date">(2021年10月27日)</div></div><div class="_popIn_recommend_article _popIn_idx2 _popIn_recommend_article_ad _popIn_recommend_has_img _popIn_recommend_img_fit"><div class="_popIn_recommend_art_img"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.uniqlo.com%2Ftw%2Fzh_TW%2Flimited_offer_kids.html%3Futm_campaign%3D21FW_MK_Halloween%26utm_source%3Dpopin%26utm_medium%3Ddisplay%26utm_content%3DNative_JPG_SP_21FW_Halloween_Kid_2%26utm_term%3DEvaluation%26tripid%3Dbca62e0909484e053af5f5033631bdd6%26popintoken%3Dbca62e0909484e053af5f5033631bdd6%26ad_click_time%3D1635871762565%26rdt%3D1&amp;data=eyJjdmlkIjoiNEFfQ0FSQVRfVW5pcWxvIiwiYyI6IjMuMCIsInR6IjoidHciLCJmIjoiMiIsIm5pZCI6IjYxN2E3NDY3OWExMDUyMWI3YTcwYWI0OSIsIm1fY2F0IjoiIiwiY2FtcGFpZ24iOiI2MTdhNzQ2NjlhMTA1MjFiN2E3MGFiNDQiLCJtZWRpYSI6Im1vbmV5LnVkbi5jb20iLCJjYXRlZ29yeSI6ImJ1c2luZXNzIiwibSI6IjI3MjY0NTI5IiwiZGV2aWNlIjoicGMiLCJsX2NhdCI6IklBQjI1LTcifQ==&amp;token=bca62e0909484e053af5f5033631bdd6&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/discovery/3c27331c1c7b0567dd474142af307251.jpeg&quot;); background-size: contain; background-repeat: no-repeat;"></a></div><div class="_popIn_recommend_art_title"><a href="https://a.popin.cc/popin_redirect/redirect?lp=https%3A%2F%2Fwww.uniqlo.com%2Ftw%2Fzh_TW%2Flimited_offer_kids.html%3Futm_campaign%3D21FW_MK_Halloween%26utm_source%3Dpopin%26utm_medium%3Ddisplay%26utm_content%3DNative_JPG_SP_21FW_Halloween_Kid_2%26utm_term%3DEvaluation%26tripid%3Dbca62e0909484e053af5f5033631bdd6%26popintoken%3Dbca62e0909484e053af5f5033631bdd6%26ad_click_time%3D1635871762565%26rdt%3D1&amp;data=eyJjdmlkIjoiNEFfQ0FSQVRfVW5pcWxvIiwiYyI6IjMuMCIsInR6IjoidHciLCJmIjoiMiIsIm5pZCI6IjYxN2E3NDY3OWExMDUyMWI3YTcwYWI0OSIsIm1fY2F0IjoiIiwiY2FtcGFpZ24iOiI2MTdhNzQ2NjlhMTA1MjFiN2E3MGFiNDQiLCJtZWRpYSI6Im1vbmV5LnVkbi5jb20iLCJjYXRlZ29yeSI6ImJ1c2luZXNzIiwibSI6IjI3MjY0NTI5IiwiZGV2aWNlIjoicGMiLCJsX2NhdCI6IklBQjI1LTcifQ==&amp;token=bca62e0909484e053af5f5033631bdd6&amp;t=1635871763924&amp;uid=66a0d9d739903c54caa1602040838150&amp;api_host=tw.popin.cc&amp;logid=09be11c0-f4d1-4d61-9c81-cff957eed762&amp;extra=m_ch_with_sz_all_ltr__pc_new_ui_addOneAd%7Cc_lc_TPE&amp;mode=20170420&amp;referer_type=organic&amp;td_client_id=68d2c5ad-7269-420f-900c-432a89ce69e9" target="_blank" rel="nofollow">UNIQLO放大五倍券！秋冬百款花色驚喜價NT$149起，還有會員獨享禮金！</a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_media">PR</div><div class="_popIn_recommend_art_date"></div></div><div class="_popIn_recommend_article _popIn_idx3 _popIn_recommend_article_cf _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://money.udn.com/money/story/5613/5855073?from=popinpc2" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/article/79a9a6a8eb171cd594e1e7a63a1dded3_160.jpg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://money.udn.com/money/story/5613/5855073?from=popinpc2">獨／樂天銀行董事長簡明仁今早辭世 享壽70歲 </a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_date">(2021年10月30日)</div></div><div class="_popIn_recommend_article _popIn_idx4 _popIn_recommend_article_cf _popIn_recommend_has_img"><div class="_popIn_recommend_art_img"><a href="https://money.udn.com/money/story/5607/5850675?from=popinpc2" style="opacity: 1; background-image: url(&quot;https://imageaws.popin.cc/article/013de0953c1c4ff240792e0d4381aebc_160.jpg&quot;);"></a></div><div class="_popIn_recommend_art_title"><a href="https://money.udn.com/money/story/5607/5850675?from=popinpc2">元宇宙 vs. 星鏈計畫 台股吸金力誰最強？ </a></div><div class="_popIn_recommend_art_category"></div><div class="_popIn_recommend_art_date">(2021年10月28日)</div></div></div></div><div class="_popIn_recommend_credit">Recommended by<div class="_popIn_recommend_credit_image"></div></div></div></div>
                      <script type="text/javascript">
                        (function() {
                          var pa = document.createElement('script'); pa.type = 'text/javascript'; pa.charset = "utf-8"; pa.async = true;
                          pa.src = window.location.protocol + "//api.popin.cc/searchbox/udn_money.js";
                          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(pa, s);
                        })();
                      </script>
                                                      </section>
                <section class="article-comments">
                  <div id="comments" class="area">
			<h3>留言</h3>
				<a name="fb_comments"></a>
		<div id="comments_head">
			<div id="fb-root"></div>
			<div style="display: inline-block;"><style>
            @font-face{
                font-family: DuckDuckGoPrivacyEssentials;
                src: url(chrome-extension://bkdgflcldnnnapblkhphbgpggdiikppg/public/font/ProximaNova-Reg-webfont.woff);
            }
            @font-face{
                font-family: DuckDuckGoPrivacyEssentialsBold;
                font-weight: bold;
                src: url(chrome-extension://bkdgflcldnnnapblkhphbgpggdiikppg/public/font/ProximaNova-Bold-webfont.woff2);
            }

            .DuckDuckGoSocialContainer a {

                color: #3969EF;

                font-weight: bold;
            }
            .DuckDuckGoSocialContainer a:hover {

                color: #3969EF;

                font-weight: bold;
            }
        </style><div class="DuckDuckGoSocialContainer" style="box-sizing: border-box; border: 1px solid rgba(0, 0, 0, 0.1); border-radius: 12px; max-width: 600px; min-height: 300px; margin: auto; display: flex; flex-direction: column; font-family: DuckDuckGoPrivacyEssentials; line-height: 1; background: rgb(255, 255, 255); color: rgb(34, 34, 34);"><div style=""><div style="display: flex; padding: 12px; max-height: 44px; border-bottom: 1px solid rgba(196, 196, 196, 0.3); border-top-color: rgba(196, 196, 196, 0.3); border-right-color: rgba(196, 196, 196, 0.3); border-left-color: rgba(196, 196, 196, 0.3);"><div style="flex-basis: 0%; min-width: 20px; height: 21px;"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACECAMAAABmmnOVAAA0aXpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjarZxpkhw5kqX/4xR1BOzLcQAFIDI36OP392BB5lY9Uy0yyWQyMsLpbgaovkVVYe781/+57l//+lcIPXeXS+t11Or5J4884uSL7r9/xvtv8Pn99/3T88/Pwl+/737/IPKtxJ/p+982f14/+X750xv9ep/11++7/vOT2H/eKPx+4/dP0ifr6/3ni+T78ft++LkQN873RR29/flS188b2a8r7n/8zr8v6/tD/+/+8o3GKu3CB6UYTwrJv//m7wqSfoc0+TPx35Aar/Np8HVJ0b1vxZ83Y0H+cnu//vT+zwv0l0X+9ZX7++r//upvix/nz/fT39ay/qwRX/zbH4Tyt++n3x8T//zB6fcVxb/+IIS4/3E7P7/v3f3e893dzJUVrT8R9RY7/HobXrhY8vT+WuVX43fh6/Z+DX51P72x5dubX/yyMEJkV64LOewwww3n/WnBuMQcT2RPYozGRul7nT0a0dgldlG/wo2NHdups5cWj2Mrc4q/ryW8zx3v8yx0PnkHXhoDb8bu/s+/3P/th/+bX+5ee0vs+++14rqiIovL0M7pv7yKDQn3Z9/KW+Bfv3623/8pfhSqmZdpmTs3OP363mKV8EdspbfPidcV/vxSKLi2f96AJeKzCxcTEjvga0gl1OBbjC0E1rGzQZMrjynHxQ6EUuLmImNOqUbXYo/6bP5OC++1scQa9W2wiY0oqabG3pBTbFbOhfhpuRNDs6SSSym1tNJdGWXWVHMttdZWBXKzpZZbabW11ttosycgsPTaW+999DniSGBgGXW00ccYc0Y3+aDJe01eP/nOiiutvMqqq62+xppG+Fi2YtWadRs2d9xpAxO77rb7Hnue4A5IcfIpp552+hlnXmLtpptvufW22++48/eu/ezqP379L3Yt/OxafDul17Xfu8Z3XWu/3iIITor2jB2LObDjTTtAQEftme8h56id0575EUmKErnIor1xO2jH2MJ8Qiw3/N67P3buP9o3V/p/tG/x/7VzTlv3/2PnHFv3z337N7u2xXP2duzLQq2pT2QfPz99utinSG3++z9H9vER0ogNiCz11FFYzM3HZH6SY2UHQOvr7LCJx9/pYxrz3JXnZbdYl+pjGens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" height="21px" style="height: 21px; width: 21px;"></div><div id="DuckDuckGoPrivacyEssentialsCTLElementTitle" style="font-family: DuckDuckGoPrivacyEssentials; line-height: 1.4; font-size: 14px; margin: auto 10px; flex-basis: 100%; height: 1.4em; flex-wrap: wrap; overflow: hidden; text-align: left;">DuckDuckGo</div><a id="DuckDuckGoPrivacyEssentialsCTLElementTitleTextButton" style="line-height: 1.4; font-size: 14px; font-weight: bold; font-family: DuckDuckGoPrivacyEssentialsBold; text-decoration: none; cursor: pointer; min-width: 100px; text-align: end; float: right; display: none; color: rgb(57, 105, 239);">Unblock comments</a></div></div><div style="display: flex; flex-direction: column; margin: auto;"><div style="font-family: DuckDuckGoPrivacyEssentialsBold; font-size: 17px; font-weight: bold; margin: 20px auto 10px; padding: 0px 30px; text-align: center;">DuckDuckGo blocked these Facebook comments</div><div style="font-family: DuckDuckGoPrivacyEssentials; font-size: 14px; line-height: 21px; margin: auto; padding: 0px 40px; text-align: center;">We blocked Facebook from tracking you when the page loaded. If you unblock these comments, Facebook will know your activity. <a aria-label="Read about this privacy protection" href="https://help.duckduckgo.com/duckduckgo-help-pages/privacy/embedded-content-protection/" style="line-height: 1.4; font-size: 14px; font-weight: bold; font-family: DuckDuckGoPrivacyEssentialsBold; cursor: pointer; text-decoration: none; color: rgb(57, 105, 239);">Learn More</a></div><div style="display: flex; margin: 20px auto 0px; padding-bottom: 36px;"><button style="border-radius: 8px; padding: 11px 22px; font-weight: bold; margin: auto; border: none; font-family: DuckDuckGoPrivacyEssentialsBold; font-size: 14px; position: relative; cursor: pointer; box-shadow: none; z-index: 2147483646; background: rgb(57, 105, 239);"><div style="display: flex; flex-direction: row; align-items: center; color: rgb(255, 255, 255);">Unblock comments</div></button></div></div></div></div>
		</div>
		<!-- /#comments_head -->

		<link href="/static/css/comments.css?s=0109" rel="stylesheet" type="text/css">
		<div id="article_id" style="display:none">5859426</div><div id="channel_id" style="display:none">1001</div>
		<div id="comments_body"><form action="/funcap/discuss/disAdd.jsp"><a name="discuss"></a><h3><span><i></i>udn 討論區</span></h3><div class="comments_rule"><a href="javascript:void(0)" class="group_btn"><span class="open_this"><b></b>規範</span><span class="close_this"><b></b>規範</span></a><div class="group"><ul><li>張貼文章或下標籤，不得有違法或侵害他人權益之言論，違者應自負法律責任。</li><li>對於明知不實或過度情緒謾罵之言論，經網友檢舉或本網站發現，經濟日報網有權逕予刪除文章、停權或解除會員資格。不同意上述規範者，請勿張貼文章。</li> <li>對於無意義、與本文無關、明知不實、謾罵之標籤，經濟日報網有權逕予刪除標籤、停權或解除會員資格。不同意上述規範者，請勿下標籤。</li> <li>凡「暱稱」涉及謾罵、髒話穢言、侵害他人權利，經濟日報網有權逕予刪除發言文章、停權或解除會員資格。不同意上述規範者，請勿張貼文章。</li> </ul></div></div> <a href="javascript:void(0)" id="face_show" title="移除表情"><img id="putedicon"><b></b></a><input type="hidden" id="post_nickname" name="post_nickname" value="guest"><p><textarea name="post_text" maxlength="500" cols="45" rows="5" class="post_text"></textarea>500字以內，目前輸入 <span class="dis_word_num">0</span> 字 <span style="color:#ef0000;font-size:13px;font: 13px/1.8 Helvetica, Arial, &quot;LiHei Pro&quot;, 新細明體, PMingLiU, sans-serif;" id="dis_msg"></span> </p><div id="emoticons"><a href="javascript:void(0)" class="post_new">發表意見</a><div id="emoticons_face"><a style="cursor:pointer;" id="emoticons_new" title="選擇表情"></a><dl><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_01.gif" title="讚拉!"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_02.gif" title="哈哈哈"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_03.gif" title="+1"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_04.gif" title="開心"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_05.gif" title="好感動"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_06.gif" title="好笑"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_07.gif" title="加油!!"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_08.gif" title="NO~~~~"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_09.gif" title="蛤？！"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_10.gif" title="OMG~"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_11.gif" title="噗～好瞎！"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_12.gif" title="踹共！！！"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_13.gif" title="有事嗎？"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_14.gif" title="無言(不予置評)"></dt><dt><img class="emoticon" src="https://j.udn.com.tw/img/emoticons_15.gif" title="怒"></dt></dl></div></div><input type="hidden" name="article_id" value="5859426"> <input type="hidden" name="art_title" value="一覺醒來資產多1兆！馬斯克登首富宣告三主流，電動車、低軌衛星、元宇宙明年誰成真？"><input type="hidden" name="art_url" value="https://money.udn.com/money/story/5607/5859426?from=edn_search_result"><input type="hidden" name="picked_icon" id="pickedicon"><input type="hidden" name="channel_id" value="1001"> </form><hr> <h3>共 <span class="discount">0</span> 則回應</h3><dl class="disl"></dl><div class="pagelink"></div>  
		</div>
		<!-- /#comments_body -->
	</div>
<div id="ec" class="area only_mobile">
		<!--
<a href="https://www.books.com.tw/products/0010873471?sloc=main" target="_blank">
   <img src="https://uc.udn.com.tw/upf/2015_money/SSI/ad/202010281_ad.jpg" width="300" height="225" alt="股債雙存獲利六堂課" title="股債雙存獲利六堂課">
</a>
-->

<!-- /129853887/udn.com/2_money/3_money-Mobile/4_money-Mobile-a01 經濟VIP Mobile第二大佈告 -->
<div id="google_ad">
<div id="div-gpt-ad-1633326636560-0" style="margin:0px auto;">
  <script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-1633326636560-0'); });
  </script>
</div>
</div></div>
                  <!-- /129853887/udn.com/money/Mobile/300*250 -->
<style>
#div-gpt-ad-1490165647547-0 { margin: 0 auto 10px;}
#div-gpt-ad-1490165647547-0 iframe { margin:auto; }
#div-gpt-ad-1490165647547-0 > div { margin: auto; display: block !important; text-align: center; }
</style>
<div id="google_ad">
<div id="div-gpt-ad-1490165647547-0">
<script>
googletag.cmd.push(function() { googletag.display('div-gpt-ad-1490165647547-0'); });
</script>
</div>
</div>                </section>
              </div>
          </section>
    ```
