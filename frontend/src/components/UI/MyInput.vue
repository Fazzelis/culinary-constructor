<template>
    <div class="wrapper">
        <input type="text" class="wrapper__input" placeholder="Название" aria-label="Поле поиска блюда" :value="modelValue" @input="updateInput">
        <MyButtonS class="wrapper__btn" title="Найти блюдо" @click="$emit('searchDish')">
            <SvgSearch />
        </MyButtonS>
    </div>
</template>

<script>
import SvgSearch from '../../assets/icons/SvgSearch.vue';
import MyButtonS from './MyButtonS.vue';

export default {
    components: {MyButtonS, SvgSearch},
    props: {
        modelValue: [String, Number],
    },
    methods: {
        updateInput(event) {
            this.$emit('update:modelValue', event.target.value)
        },
    },
}
</script>

<style lang="less">
.wrapper{
    position: relative;
    max-width: 700px;
    width: 100%;

    &:hover {
        .wrapper__input {
            border-color: @orange;
        }
    }
    
    &__input{
        width: 100%;
        height: 50px;
        padding: 20px 8px 20px 30px;
        background-color: @light;
        border: 3px solid @light;
        border-radius: 12px;
        transition: all 0.3s;
    }

    &__btn{
        position: absolute;
        right: 8px;
        top: 6px;
        color: @light;
    }

}
</style>