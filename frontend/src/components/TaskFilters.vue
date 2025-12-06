<template>
  <div class="flex gap-3 mb-3">
    <AutoComplete v-model="filters.status" :suggestions="statuses"  optionLabel="label" optionValue="value" dropdown placeholder="Status" />
    <!-- <Dropdown v-model="filters.status" :options="statuses" optionLabel="label" optionValue="value" placeholder="Status" /> -->
    <!-- <InputText v-model="filters.search" placeholder="Pesquisar título..." /> -->
     <AutoComplete v-model="filters.search" placeholder="Pesquisar título..." />
  </div>
</template>

<script setup>
import AutoComplete from 'primevue/autocomplete';
// import { Dropdown } from 'primevue/dropdown'
// import { InputText } from 'primevue/inputtext'

const props = defineProps({
  filters: Object // v-model compartilhado com o pai
})

const statuses = [
  { label: 'Todos', value: '' },
  { label: 'Pendente', value: 'Pendente' },
  { label: 'Concluída', value: 'Concluída' }
]
</script>
