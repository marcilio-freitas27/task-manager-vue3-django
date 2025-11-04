<script setup>
import { onMounted, ref } from 'vue';

// Options API

// export default {
//   data() {
//     return {
//       nome: 'Fulano'
//     };
//   },
//   mounted() {
    
//   },
//   methods: {
//     exibirMensagem() {
//       alert('Componente montado com sucesso!');
//     }
//   }
// };

// Composition API
// como alternativa para o data(){return {suasvariaveis:'valor'}}
const nome = ref('Fulano');

// como alternativa para o methods:{ suafuncao(){ressultado}}
function exibirMensagem() {
  alert('Componente montado com sucesso!');
}

// como alternativa para o mounted(){ }
//ciclo de vida do Vue
onMounted(() => {
  exibirMensagem();
});

</script>

<template>
  <h1>You did it, {{ nome }}!</h1>
  <p>
    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the
    documentation
  </p>
  <button type="button" @click="exibirMensagem()">Mensagem de sucesso</button>
</template>

<style scoped></style>
