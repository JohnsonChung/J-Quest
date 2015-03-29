$(function() {
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
    var templateCaches = {};

    /* cache elements */
    var $main = $('#main');
    var $side = $('#side');

    var hbs = {
        cache: {},
        registerPartial: function(e) {
            Handlebars.registerPartial(e);
            //
            // undefined
            //
        },
        compile: function(e) {
            Handlebars.compile(e);
            //
            // undefined
            //
        },
        initialize: function() {
            this.cacheTemplate(templates);
            this.cache = templateCaches;
        },
        /* 將所有 template.hbs 塞到 templateCaches 裡面 */
        cacheTemplate: function(templates) {
            $.each(templates, function(index, value) {
                $.get('js/templates/' + value + '.hbs').then(function(data) {
                    var o = {};
                    o[value] = data;
                    $.extend(templateCaches, o);
                });
            });
        },
        /* 點擊按鈕後切換 template */
        change: function(target) {
            console.log("==== Start ====");
            var template ={};
            if (target.lastIndexOf("/") != -1) {
                console.log("讀取次級樣板...")
                var parts = target.split('/');
                var body = parts[0];
                var partial = parts[parts.length - 1];
                template = Handlebars.compile(this.cache[target]);
                Handlebars.registerPartial("partial", this.cache[body + '/' + partial]);

                console.log('已讀取次級樣板 [' + partial + "].");

            } else {
                if (this.cache[target+'/'+target+'-index']) {
                    console.log('發現目標有次級樣板...');                    
                    template = Handlebars.compile(this.cache[target+'/'+target+'-index']);
                    console.log('已讀取次級樣板 ['+target+ '-index]');
                } else { template = Handlebars.compile(this.cache[target]);}
            }

            $main.html(template());
            console.log("切換頁面: 已讀取樣板 [" + target + "].");
            console.log("==== End ====");
        }
    };

    window.hbs = hbs;
    hbs.initialize();

    $.get('js/templates/sideNav.hbs').then(function(data) {
        $side.html(Handlebars.compile(data));
    });
});
