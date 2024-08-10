<template>
  <div class="home">
    <EditProduct msg="Edit Product"/>
  </div>
</template>

<script>
// @ is an alias to /src
import EditProduct from '@/components/EditProduct.vue'

export default {
  name: 'EditProductView',
  components: {
    EditProduct
  }
}
</script>