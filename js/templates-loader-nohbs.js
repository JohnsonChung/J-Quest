$(function() {
    // 需要讀取的樣板列表
    var templates = [
        "templateBody",
        "sideNav",
        "about",
        "campaign",
        "concept",
        "contact",  
        "faq",
        "howto",
        "privacy",
        "recruit",
        "recruit/recruit-index",
        "recruit/recruit-form",
        "recruit/recruit-manager",
        "recruit/recruit-merit",
        "recruit/recruit-oshiete",
        "recruit/recruit-parttimer",
        "recruit/recruit-pts",
        "recruit/recruit-voice",
        "recruit/recruit-work",
        "service",
        "shop",
    ];
    // 快取樣板
    var templateCaches = {};

    // 快取 Elements
    var $main = $('#main');
    var $side = $('#side');

    var hbs = {
        // 快取樣板
        cache: {},
        initialize: function() {
            this.cacheTemplate(templates);
            this.cache = templateCaches;
        },
        /* 將所有 template.hbs 快取到 templateCaches 裡面 */
        cacheTemplate: function(templates) {
            $.each(templates, function(index, value) {
                $.get('js/templates/' + value + '.hbs').then(function(data) {
                    var o = {};
                    o[value] = data;
                    $.extend(templateCaches, o);
                });
            });
        },
        /* 點擊按鈕後切換樣板 */
        change: function(target) {
            console.log("==== Start ====");
            var template ={};

            // 如果有 "/" 則讀取次級樣板 (例如： recruit/recruit-form )
            if (target.lastIndexOf("/") != -1) {
                console.log("讀取次級樣板...")
                var parts = target.split('/');
                var body = parts[0];
                var partial = parts[parts.length - 1];
                template = Handlebars.compile(this.cache[body]);
                Handlebars.registerPartial("partial", this.cache[body + '/' + partial]);

                console.log('已讀取次級樣板 [' + partial + "].");

            } else {
                // 檢查有沒有次級樣板 (例如： templates/recruit/recruit-index.hsb )
                if (this.cache[target+'/'+target+'-index']) {
                    console.log('發現目標有次級樣板...');       
                    template = Handlebars.compile(this.cache[target]);
                    Handlebars.registerPartial("partial", this.cache[target+'/'+target+'-index']);
                    console.log('已讀取次級樣板 ['+target+ '-index]');
                } 
                // 讀取一般樣板 ( 例如： about.hsb )
                else { 
                    template = Handlebars.compile(this.cache[target]);
                }
            }
            // 輸出樣板
            $main.html(template());
            console.log("切換頁面: 已讀取樣板 [" + target + "].");
            console.log("==== End ====");
        }
    };

    window.hbs = hbs;
    hbs.initialize();

    // 讀取左方瀏覽列表
    $.get('js/templates/contact.hbs').then(function(data) {
        $main.html(data);
    });
    // 讀取左方瀏覽列表
    $.get('js/templates/sideNav.hbs').then(function(data) {
        $side.html(data);
    });
});
