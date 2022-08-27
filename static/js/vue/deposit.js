const app = new Vue({
    el: '#credit-calc',
    delimiters: ['[[', ']]'],
    data: {
        sum: SUM_MIN,
        month: DATE_MIN,
        error_msg: '',
        error_msg_month: '',
        isDisableButton: false,

        // TOTAL TABLE

        monthly_pay: 0, // Месячная оплата (для таблицы)
        month_percent: 0, // Месячный процент (для таблицы)
        total_sum: 0, // Итого (для таблицы)
        details: [], // Детально

        // CALCULATING
        sum_difference: 0, // Остаток после оплаты кредита (для калькулятора)
        selectedRate: null,

        // CURRENCY
        currencies: [],

        currencySelectIsActive: false,
        displayCurrency: 'none',
        selectedCurrency: {'name': 'Валюта', 'value': ''},
    },
    mounted: function () {
        this.currencies = CURRENCIES;
        this.getSelectedCurrency()
    },
    methods: {
        getSelectedCurrency: function () {
            if (REQUEST_PATH.includes('KGS')) {
                this.selectedCurrency = CURRENCIES[0]
            }
            else if (REQUEST_PATH.includes('USD')) {
                this.selectedCurrency = CURRENCIES[1]
            }
            else {
                this.selectedCurrency = {'name': 'Сом', 'value': 'KGS'}
            }

        },

        calculate: function () {
            if (this.selectedCurrency.value === 'KGS') {
                this.selectRateKGS()
            }
            else if (this.selectedCurrency.value === 'USD') {
                this.selectRateUSD()
            }
            else {
                this.error_msg = 'Выберите необходимую валюту'
                return
            }
            sum = this.sum
            percent = this.selectedRate.rate
            percent = parseFloat(percent.replace(',', '.'))
            console.log(percent)
            month = this.month
            percent = percent / 100;
            this.monthly_pay = sum * percent / 360 * 30;
            this.total_sum = this.monthly_pay * month;

            this.monthly_pay = Number(this.monthly_pay.toFixed(2))
            this.total_sum = Number(this.total_sum.toFixed(2))

            this.getDetails()
        },

        getDetails: function () {
            let details = []
            this.sum_difference = this.sum
            for(let i = 1; i <= this.month; i++) {
                this.sum_difference = Number(this.sum_difference) + Number(this.monthly_pay)
                details.push({
                    'month': i,
                    'monthly_payment': this.monthly_pay,
                    'difference': Number(this.sum_difference.toFixed(2))
                })
            }
            if (!!details) this.details = details
        },

        selectRateKGS: function () {
            console.log(RATES_KGS)
            for (i=0; i<RATES_KGS.length; i++) {
                rate = RATES_KGS[i]

                if (Number(rate.duration_from) <= Number(this.month) && Number(this.month) <= Number(rate.duration_to)) {
                    this.selectedRate = rate;
                    break;
                }
                else {
                    this.selectedRate = null;
                }
            }
        },

        selectRateUSD: function () {
            for (i=0; i<RATES_USD.length; i++) {
                rate = RATES_USD[i]

                if (Number(rate.duration_from) <= Number(this.month) && Number(this.month) <= Number(rate.duration_to)) {
                    this.selectedRate = rate;
                    break
                }
                else {
                    this.selectedRate = null;
                }
            }
        },

        selectCurrency: function (currency) {
            this.selectedCurrency = currency
            this.toggleCurrency()

        },

        toggleCurrency: function () {
            this.currencySelectIsActive = !this.currencySelectIsActive
            if (this.displayCurrency === 'none') {
                this.displayCurrency = 'block'
            }
            else {
                this.displayCurrency = 'none'
            }
        },

        changeSum: function (sum) {
            if (!!sum) this.sum = sum
        },

        changeMonth: function (month) {
            if (!!month) this.month = month
        },

        checkSum: function () {
            if (this.sum > SUM_MAX || this.sum < SUM_MIN) {
                this.isDisableButton = true;
                this.error_msg = 'Размер депозита не может быть меньше ' + SUM_MIN + ', и больше ' + SUM_MAX
            } else {
                this.isDisableButton = false;
                this.error_msg = ''
            }
        },
        checkMonth: function () {
            if (this.month > DATE_MAX || this.month < DATE_MIN) {
                this.isDisableButton = true;
                this.error_msg_month = 'Срок депозита не может быть меньше ' + DATE_MIN + ', и больше ' + DATE_MAX
            } else {
                this.isDisableButton = false;
                this.error_msg_month = ''
            }
        }
    }
})

const deposit = new Vue({
    el: '#credit_modal',
    delimiters: ['[[', ']]'],
    data: {
        name: null,
        last_name: null,
        middle_name: null,
        email: null,
        phone: null,
        address: null,
        sum: 1000,

        isCheckbox: false,
        regions: [],
        selectedRegion: {name: 'Выберите область'},
        regionSelectIsActive: false,
        displayRegionSelect: 'none',

        districts: [],
        selectedDistrict: {name: 'Выберите район'},
        districtSelectIsActive: false,
        displayDistrictSelect: 'none',

        credits: DEPOSITS,
        selectedCredit: {name: 'Выберите депозит'},
        creditSelectIsActive: false,
        displayCreditSelect: 'none',
    },
    mounted: function () {
        this.getData();
        this.parseDepositName()
    },
    methods: {
        toggleCheckbox: function () {
            this.isCheckbox = !this.isCheckbox;
        },

        parseDepositName: function () {
            for(let i=0; i<this.credits.length; i++) {
                this.credits[i].name = this.credits[i].name.replace(/&quot;/g,'"')
            }
        },
        getData: async function() {
            let regions = await get_regions();
            if (!!regions) this.regions = regions;
            console.log(this.credits)
        },

        sendRequest: async function() {
            data = {
                "deposit": this.selectedCredit.name,
                "name": this.name,
                "last_name": this.last_name,
                "middle_name": this.middle_name,
                "phone": this.phone,
                "email": this.email,
                "region": this.selectedRegion.name,
                "district": this.selectedDistrict.name,
                "address": this.address,
                "sum": this.sum
            }
            let credit_modal = document.getElementById('credit_modal');
            credit_modal.classList.remove('show')

            let finish_modal = document.getElementById('finishmodal');
            finish_modal.style.opacity = 100;
            finish_modal.style.visibility = 'visible';
            await create_deposit_app(data);
        },

        closeFinishModal: function () {
            let elem = document.getElementById('finishmodal');
            elem.style.opacity = 0;
            elem.style.visibility = 'hidden';
        },

        selectRegion: function (region){
            this.selectedRegion = region
            this.region = region.id
            this.districts = region.district_list
            this.regionSelectIsActive = false
            this.selectedCity = {name: 'Город'}
            this.setRegionSelect()
        },
        setRegionSelect: function () {
            if (this.displayRegionSelect === 'block') {
                this.displayRegionSelect = 'none';
                this.regionSelectIsActive = false;
            } else {
                this.displayRegionSelect = 'block';
                this.regionSelectIsActive = true;
            }
        },


        selectDistrict: function (district){
            this.selectedDistrict = district
            this.district = district.id
            this.districtSelectIsActive = false
            this.setDistrictSelect()
        },
        setDistrictSelect: function () {
            if (this.displayDistrictSelect === 'block') {
                this.displayDistrictSelect = 'none';
                this.districtSelectIsActive = false;
            } else {
                this.displayDistrictSelect = 'block';
                this.districtSelectIsActive = true;
            }
        },


        selectCredit: function (credit){
            this.selectedCredit = credit
            this.credit = credit.id
            this.creditSelectIsActive = false
            this.setCreditSelect()
        },
        setCreditSelect: function () {
            if (this.displayCreditSelect === 'block') {
                this.displayCreditSelect = 'none';
                this.creditSelectIsActive = false;
            } else {
                this.displayCreditSelect = 'block';
                this.creditSelectIsActive = true;
            }
        },

    }
});