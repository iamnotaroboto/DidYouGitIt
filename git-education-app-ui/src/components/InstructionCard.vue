<template>
  <md-card>
    <slot></slot>
  </md-card>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'InstructionCard',
  props: {
    instruction: String,
  },
});
</script>
