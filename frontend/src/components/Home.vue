<template lang="html">
    <div class="container relative w-full bg-gradient-to-r from-green-400 to-blue-500">
        <main class="min-h-screen">
            <!-- Header -->
            <div id="header" class="mx-5 pt-5">
                <div class="pt-5 flex flex-col justify-center rounded-xl border border-black bg-gradient-to-br from-black via-blue-800 to-black">
                    <label id ="main-tittle" class="text-center text-white font-semibold my-2 mb-8 text-7xl text-">
                    Guía de precio de carros usados
                    </label>
                </div>
                <div class="pt-12">
                    <label class="text-xl font-semibold">
                        Ingrese información del vehículo:
                    </label>
                </div>
            </div>
            <!-- Body -->
            <div id="body" class="mt-5 mx-5 mb-5 lg:flex lg:flex-row md:flex md:flex-col">
                <div class="lg:w-112 md:w-full">
                    <form
                      @submit.prevent="estimateCarPrice"
                      class="px-8 py-5 space-y-2 rounded-xl bg-gray-100"
                    >
                      <!-- Brand field -->
                      <div>
                        <label class="text-m font-bold text-gray-600 block"> Marca: </label>
                        <input
                          type="text"
                          name="brand"
                          v-model="brand"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Password field -->
                      <div class="">
                        <label class="text-m font-bold text-gray-600 block"> Modelo: </label>
                        <input
                          type="text"
                          name="model"
                          v-model="model"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Year field -->
                      <div class="">
                        <label class="text-m font-bold text-gray-600 block"> Año: </label>
                        <input
                          type="number"
                          name="brand"
                          v-model="year"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Kilometers field -->
                      <div class="">
                        <label class="text-m font-bold text-gray-600 block"> Kilometraje: </label>
                        <input
                          type="number"
                          name="kilometers"
                          v-model="kilometers"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Motor field -->
                      <div class="">
                        <label class="text-m font-bold text-gray-600 block"> Motor: </label>
                        <input
                          type="text"
                          name="motor"
                          v-model="motor"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Transmission field -->
                      <div class="">
                        <label class="text-m font-bold text-gray-600 block"> Transmisión: </label>
                        <select
                          name="transmission"
                          v-model="transmission"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500">
                            <option value="Automatica">Automática</option>
                            <option value="Mecanica">Mecánica</option>
                            <option value="Automatica secuencial">Automática secuencial</option>
                        </select>
                      </div>
                      <!-- Submit button -->
                      <div class="pt-3 flex justify-center">
                        <button
                          class="py-2 px-4 bg-blue-500 hover:bg-blue-600 rounded-2xl text-white flex justify-center"
                        >
                          Predecir precio
                        </button>
                      </div>
                    </form>
                    <div class="lg:w-112 border bg-gray-100 rounded-xl mt-5 px-8 py-5 font-semibold md:w-full text-lg">
                        El precio estimado para su carro es: &nbsp; <label class="text-green-500 text-xl"> {{ price }} </label>
                    </div>
                </div>        
                <!-- rotating car gif -->
                <div class="w-full flex flex-col justify-center lg:ml-10">
                    <img @click="changeCarImg" id="carImg" src="https://drive.google.com/uc?export=view&id=1Qaoqn1xozn2kNRSFYsKiSNtdezcN-L_-" />
                </div>
            </div>
            <!-- Footer -->
            <div id="footer" class="w-full bg-gray-100 h-16 mt-16">
                <div class="p-5 text-gray-500"> © 2021 ICESI University </div>
            </div>
        </main>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Main",
  data() {
    return {
      brand: "",
      model: "",
      year: "",
      kilometers: "",
      motor: "",
      transmission: "",
      price: "",
      img_count: 0,
      cars_imgs: [
        "https://drive.google.com/uc?export=view&id=1Qaoqn1xozn2kNRSFYsKiSNtdezcN-L_-",
        "https://drive.google.com/uc?export=view&id=1y0PZkQ5PNdlax_51j-VbvW_re7a11cb_",
        "https://drive.google.com/uc?export=view&id=15QEtVDUfzi-APJzbY6hCPG3SHZn4ZUSa",
        "https://drive.google.com/uc?export=view&id=1TA8lquwfZCObw6woYEFfEygd77u4z4-W",
        "https://drive.google.com/uc?export=view&id=1jeUZzbC1W8ZKJGGUjSbdVcqTt3r0GLTT",
        "https://drive.google.com/uc?export=view&id=1sQAC2_PGJlG3cha_LV1k1rB9l5leqBQK",
        "https://drive.google.com/uc?export=view&id=16ix8mPDheXOnFm3G0DAFSBks8rLal5m1",
      ],
    };
  },
  methods: {
    changeCarImg() {
      if (this.img_count == 6) {
        this.img_count = 0;
        document.getElementById("carImg").src = this.cars_imgs[this.img_count];
      } else {
        this.img_count += 1;
        document.getElementById("carImg").src = this.cars_imgs[this.img_count];
      }
    },
    estimateCarPrice() {
      const path = "http://localhost:5000/api/v1.0/estimateCarPrice";
      axios
        .post(path, {
          brand: this.brand,
          model: this.model,
          year: this.year,
          kilometers: this.kilometers,
          motor: this.motor,
          transmission: this.transmission,
        })
        .then((response) => {
          this.price = "$ " + response.data;
        })
        .catch((error) => {
          console.error(error);
        });

      // clear fields
      this.brand = "";
      this.model = "";
      this.year = "";
      this.kilometers = "";
      this.motor = "";
      this.transmission = "";

      this.changeCarImg();
    },
  },
  created() {},
};
</script>