<template>
  <div class="question-container">
    <div class="md-layout md-gutter">
      <div class="md-layout-item instruction-card">
        <InstructionCard>
          <component :is="instructionComponents.get(currentRouteName)" />
        </InstructionCard>
      </div>
    </div>
    <br />
    <div v-if="currentRouteName !== 'intro'" class="md-layout-itemmd-layout md-gutter">
      <div class="md-layout-item input-card">
        <InputCard
          :questionId="currentRouteName"
          v-on:submit-answer="updateOutput"
        />
      </div>
      <br />
      <div class="md-layout-item output-card">
        <OutputCard
          :questionId="currentRouteName"
        />
      </div>
    </div>
    <div class="next-btn-container"
      v-if="currentRouteName !== 'intro' &&
      currentRouteName !== 'scenario5' ">
      <md-button
        class="md-raised md-primary"
        v-on:click="onNext()">Next
      </md-button>
    </div>
    <div class="dialog-container">
      <md-dialog :md-active.sync="showDialog">
        <md-dialog-title>
          You have anwsered {{ correctCount }} out of
          {{ instructionComponents.size }} questions correctly
        </md-dialog-title>
        <md-dialog-content>
          You can continue work on the questions and share this course with your friends.
          <br>
          <br>
          Here is our link:
          <br>
          <span class="md-body-2">http://didyougitit.s3-website-us-east-1.amazonaws.com</span>
        </md-dialog-content>
        <md-dialog-actions>
          <md-button class="md-primary" @click="showDialog = false">OK</md-button>
        </md-dialog-actions>
      </md-dialog>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapActions } from 'vuex';
import { actionType, QuestionStatus } from '../store';
import InstructionCard from '../components/InstructionCard.vue';
import InputCard, { OutputEvent } from '../components/InputCard.vue';
import OutputCard from '../components/OutputCard.vue';
import Intro from '../components/instructions/Intro.vue';
import Q1Instruction from '../components/instructions/Q1Instruction.vue';
import Q2Instruction from '../components/instructions/Q2Instruction.vue';
import Q3Instruction from '../components/instructions/Q3Instruction.vue';
import Q4Instruction from '../components/instructions/Q4Instruction.vue';
import Q5Instruction from '../components/instructions/Q5Instruction.vue';
import CaseStudy1 from '../components/instructions/CaseStudy1.vue';
import CaseStudy2 from '../components/instructions/CaseStudy2.vue';
import CaseStudy3 from '../components/instructions/CaseStudy3.vue';
import CaseStudy4 from '../components/instructions/CaseStudy4.vue';
import CaseStudy5 from '../components/instructions/CaseStudy5.vue';


export default Vue.extend({
  name: 'Question',
  data: () => ({
    currentRouteName: 'intro',
    instructionComponents: new Map([
      ['intro', Intro],
      ['question1', Q1Instruction],
      ['question2', Q2Instruction],
      ['question3', Q3Instruction],
      ['question4', Q4Instruction],
      ['question5', Q5Instruction],
      ['scenario1', CaseStudy1],
      ['scenario2', CaseStudy2],
      ['scenario3', CaseStudy3],
      ['scenario4', CaseStudy4],
      ['scenario5', CaseStudy5],
    ]),
    showDialog: false,
    finishedCount: 0,
    correctCount: 0,
  }),
  computed: {
    progress(): Map<string, QuestionStatus> {
      return this.$store.state.progress;
    },
  },
  components: {
    InstructionCard,
    InputCard,
    OutputCard,
  },
  watch: {
    $route(to, from) {
      this.currentRouteName = to.name;
    },
  },
  methods: {
    ...mapActions({
      updateProgress: actionType.UPDATE_PROGRESS,
    }),
    updateOutput(event: OutputEvent) {
      const questionStatus: QuestionStatus = {
        status: event.isCorrect ? 'correct' : 'incorrect',
        expectedInput: event.expectedInput,
        userInput: event.userInput,
        textFeedback: event.textFeedback,
      };
      this.updateProgress({ questionId: event.questionId, status: questionStatus });
      const statusList = Array.from((this.progress as Map<string, QuestionStatus>).values());
      this.finishedCount = statusList.reduce((acc, cur) => (acc + (cur.status !== 'unfinished' ? 1 : 0)), 0);
      this.correctCount = statusList.reduce((acc, cur) => (acc + (cur.status === 'correct' ? 1 : 0)), 0);
      if (this.finishedCount === (this.instructionComponents as Map<string, any>).size - 1) {
        this.showDialog = true;
      }
    },
    onNext() {
      let nextRoute = '';
      switch (this.currentRouteName) {
        case 'question1':
          nextRoute = 'q2';
          break;
        case 'question2':
          nextRoute = 'q3';
          break;
        case 'question3':
          nextRoute = 'q4';
          break;
        case 'question4':
          nextRoute = 'q5';
          break;
        case 'question5':
          nextRoute = 'c1';
          break;
        case 'scenario1':
          nextRoute = 'c2';
          break;
        case 'scenario2':
          nextRoute = 'c3';
          break;
        case 'scenario3':
          nextRoute = 'c4';
          break;
        case 'scenario4':
          nextRoute = 'c5';
          break;
        default:
      }
      this.$router.push(nextRoute).catch((err) => {});
    },
  },
  mounted() {
    this.currentRouteName = this.$router.history.current.name;
    // init question status
    const qIds: string[] = Array.from(this.instructionComponents.keys());
    qIds.forEach((id) => {
      const questionStatus: QuestionStatus = {
        status: 'unfinished',
        userInput: '',
        expectedInput: '',
        textFeedback: '',
      };
      this.updateProgress({ questionId: id, status: questionStatus });
    });
  },
});
</script>

<style lang="scss" scoped>
.instruction-card {
  max-width: 100vw;
}
.question-container {
  padding: 15px;
}
.next-btn-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: 20px;
  button {
    margin: 0
  }
}
</style>
