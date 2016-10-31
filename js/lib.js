function loadStores($select) {
    $.get("https://www.j-quest.jp/contact3/stores", function(data) {
        if($.isArray(data) && data.length) {
            for(var i = 0;i < data.length;i++) {
                var prefecture = data[i];
                var stores = prefecture.stores;
                var $optgroup = $("<optgroup/>").attr("label", prefecture.name);
                for(var j = 0;j < stores.length;j++) {
                    var store = stores[j];
                    var $option = $("<option/>").attr("value", store.id).html(store.name);
                    $optgroup.append($option);
                }
                $select.append($optgroup);
            }
        } else {
            console.error('loadStores failed', data);
        }
    });
}