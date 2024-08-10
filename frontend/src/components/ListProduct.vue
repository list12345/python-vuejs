<template>
  <div>
    <section>
      <h1>Products</h1>
      <hr/><br/>
      <div>
        <div v-for="product in products" :key="product.id" class="products">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Product Name:</strong> {{ product.name }}</li>
                <li><strong>Price:</strong> {{ product.price }}</li>
                <li><router-link :to="{name: 'edit_product', params:{id: product.id}}">Edit</router-link></li>
                <li><router-link :to="{name: 'delete_product', params:{id: product.id}}">Delete</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      products: [],
    };
  },
  methods: {
    editProduct(product) {
      axios.put('/products/' + product.id).then((response) => {
      console.log(response)
    });
    },
    deleteProduct(productId) {
      axios.delete('/products/' + productId).then((response) => {
      console.log(response)
    });
    },
  },
  mounted() {
    // Fetch Products from the server or an API
    // and assign them to the 'Products' data property
    axios.get('/products').then((response) => {
      this.products = response.data;
    });
  },
});
</script>
