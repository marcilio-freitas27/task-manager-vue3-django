import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import Datatable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import AutoComplete from 'primevue/autocomplete';
import Aura from '@primeuix/themes/aura';

const app = createApp(App)

app.component('Datatable', Datatable);
// app.component('InputText', InputText);
app.component('AutoComplete', AutoComplete);
app.component('Column', Column);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

app.use(router);


app.mount('#app')
