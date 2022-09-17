axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const ORIGIN = location.origin

let headers = {'X-CSRFToken': 'csrftoken',}

const axi = axios.create({
    baseURL: ORIGIN,
    headers: headers
});

function get_regions() {
    return axi.get('/api/regions/')
        .then(response => response.data)
        .catch(() => console.log('Getting regions error.'))
}


function create_credit_app(data) {
    return axi.post('/api/credit-application/', data)
        .then(response => response.data)
        .catch(() => console.log('Create financing error.'))
}


function create_deposit_app(data) {
    return axi.post('/api/deposit-application/', data)
        .then(response => response.data)
        .catch(() => console.log('Create deposit error.'))
}
