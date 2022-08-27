const form = new Vue({
    el: '#checkboxForm',
    data: {
        isCheckbox: false,

    },
    methods: {
        toggleCheckbox: function () {
            this.isCheckbox = !this.isCheckbox;
        },
    }
});
