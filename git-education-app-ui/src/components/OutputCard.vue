<template>
  <md-card>
    <md-card-header>
      <div class="md-title">Output</div>
      <div v-if="hasError" class='error indicator'>INCORRECT</div>
      <div v-if="!hasError && userInput && expectedInput" class='success indicator'>CORRECT</div>
    </md-card-header>
    <md-card-content class="output-card-content">
      <div v-if="!userInput || !expectedInput">
        <span class="md-caption">
          Submit your answer first to compare it with the correct answer.
        </span>
      </div>
      <div v-if="userInput && expectedInput">
        <div>Your answer:</div>
        <div class="code"><code
            v-bind:style="hasError ? { backgroundColor: '#ff5252' } : {}">{{ userInput }}</code>
        </div>
        <span class="feedback md-caption">Hint: {{ textFeedback }} </span>
        <div
          class="answer-toggle"
          v-if="!shouldShowAnswer"
          v-on:click="toggleAnswer()">
          see answer
        </div>
        <div v-if="shouldShowAnswer">
          <div><code>{{ expectedInput }}</code></div>
        </div>
        <span
          class="answer-toggle"
          v-if="shouldShowAnswer"
          v-on:click="toggleAnswer()">
          hide answer
        </span>
      </div>
    </md-card-content>
  </md-card>
</template>
<script lang="ts">
import Vue from 'vue';
import { mapState, mapActions } from 'vuex';
import { actionType, QuestionStatus } from '../store';

export default Vue.extend({
  name: 'OutputCard',
  props: {
    questionId: String,
  },
  watch: {
    questionId() {
      this.shouldShowAnswer = false;
    },
  },
  data() {
    return {
      shouldShowAnswer: false,
    };
  },
  computed: {
    questionStatus(): QuestionStatus {
      return this.$store.state.progress.get(this.questionId);
    },
    hasError() {
      return this.questionStatus ? this.questionStatus.status === 'incorrect' : false;
    },
    userInput() {
      return this.questionStatus ? this.questionStatus.userInput : null;
    },
    expectedInput() {
      return this.questionStatus ? this.questionStatus.expectedInput : null;
    },
    textFeedback() {
      return this.questionStatus ? this.questionStatus.textFeedback : null;
    },
  },
  methods: {
    ...mapActions({
      updateProgress: actionType.UPDATE_PROGRESS,
    }),
    toggleAnswer() {
      this.shouldShowAnswer = !this.shouldShowAnswer;
    },
  },
});
</script>
<style lang="scss" scoped>
  .md-card-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    .indicator {
      margin-top: 8px;
      padding: 8px;
      color: white;
    }
    .error {
      background-color: #ff5252;
    }
    .success {
      background-color: #54e75c;
    }
  }
  .code {
    margin: 10px 0 15px 0;
  }
  .feedback {
    margin-bottom: 10px;
  }
  .answer-toggle {
    cursor: pointer;
    color: var(--md-theme-default-primary-on-background, #448aff);
  }

</style>
