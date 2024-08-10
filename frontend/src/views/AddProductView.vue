<template>
  <div class="home">
    <AddProduct msg="Add Product"/>
  </div>
</template>

<script>
// @ is an alias to /src
import AddProduct from '@/components/AddProduct.vue'

export default {
  name: 'AddProductView',
  components: {
    AddProduct
  }
}
</script>
