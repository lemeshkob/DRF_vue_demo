new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        'apptitle': 'Django Vue.js shopping cart',
        'products': []
    },
    methods: {
        addProduct: function () {
            var NewProduct = {
                title: this.title.trim(),
                price: this.price.trim()
            };

            this.$http.post('http://127.0.0.1:8000/products/', NewProduct);
        },
        removeProduct: function (index) {
            this.$http.delete('http://127.0.0.1:8000/products/'.concat(this.products[index].id));
            this.product.splice(index, 1);
        }
    },
    ready: function () {
        this.$http.get('127.0.0.1:8000/products').then(function (response) {
                this.products = response.data;
            },
            function (response) {
                console.log(response);
            });
    }
});