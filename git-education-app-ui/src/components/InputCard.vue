<template>
  <md-card>
    <md-card-header>
      <div class="md-title">User Input</div>
    </md-card-header>
    <md-card-content>
      <md-field>
        <label>Enter your answer here</label>
        <md-textarea v-model="userInput"></md-textarea>
      </md-field>
      <md-card-actions>
        <md-button
          class="md-raised md-primary"
          v-bind:disabled="userInput===''" v-on:click="onSubmit()">Submit</md-button>
      </md-card-actions>
    </md-card-content>
  </md-card>
</template>

<script lang='ts'>
import Vue from 'vue';
import { getAnswer, TextAnswerRes } from '../services/QuestionService';

export interface OutputEvent {
  questionId: string,
  userInput: string,
  expectedInput: string,
  isCorrect: boolean,
  textFeedback: string,
}

export default Vue.extend({
  name: 'InputCard',
  props: {
    questionId: String,
  },
  watch: {
    questionId() {
      this.userInput = '';
    },
  },
  data: () => ({
    userInput: '',
  }),
  methods: {
    async onSubmit() {
      const res: TextAnswerRes = await getAnswer(this.questionId, this.userInput);
      const event: OutputEvent = {
        questionId: this.questionId,
        userInput: this.userInput,
        expectedInput: res.answer,
        isCorrect: res.isCorrect,
        textFeedback: res.textFeedback,
      };
      this.$emit('submit-answer', event);
    },
  },
});
</script>

<style lang="scss" scoped>
</style>
