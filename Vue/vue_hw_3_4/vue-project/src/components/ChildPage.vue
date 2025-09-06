<script setup>
// 1. props로 받을 데이터 객체를 명시
const props = defineProps({
  childData: Object
})

// 2. 부모에게 'giveMeAllowance' 이벤트를 보냄
const emit = defineEmits(['giveMeAllowance'])

// 3. 버튼 클릭 시 실행될 함수를 정의
const requestAllowance = () => {
  // 정의한 이벤트를 발생시키고, 어떤 자식인지 알려줌
  emit('giveMeAllowance', props.childData)
}
</script>

<template>
  <div style="border: 1px solid lightgray; padding: 10px; margin-top: 10px;">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childData.name }}</p>
    <p>나이 : {{ childData.age }}</p>
    <p>용돈 : {{ childData.balance }}</p>
    <button @click="requestAllowance">용돈 주세요</button>
  </div>
</template>