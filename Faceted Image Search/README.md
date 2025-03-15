# 🍽️ **Faceted Image Search: Food Photography Collection**  

## INFO 202: Information Organization and Retrieval  
## UC Berkeley, 2024  

---

## 📌 **Overview**  
This project demonstrates the application of **faceted search and metadata design** in a food photography collection.  

The system enables users to intuitively browse and search for food images categorized by **meal type, cuisine, and dietary preference** using **Algolia's faceted search**.  

---

## 🎯 **Project Goal**  
The goal of this project is to create a structured **image search experience** optimized for **food lovers, bloggers, chefs, and marketers**.  
By implementing a **hierarchical faceted classification**, users can explore food images with **multiple levels of categorization**.  

### 🔍 **Why This Matters for Product Management**  
✔ **Design user-friendly search experiences** using metadata and taxonomy.  
✔ **Structure large datasets** into logical hierarchies for better UX.  
✔ **Work with Algolia and JSON data** for scalable search solutions.  
✔ **Apply product thinking** by optimizing navigation for target users.  

---

## 🔑 **Features**  
✔ **Faceted Search**: Users can navigate images using structured facets such as:  
   - **Meal Type**: Breakfast, Lunch, Dinner  
✔ **Hierarchical Metadata**: Three-level categorization for refined search results.  
✔ **JSON Metadata Format**: Organized dataset for easy scalability and search integration.  
✔ **Algolia Integration**: Hosted search interface powered by **Algolia** for fast, user-friendly searching.  

---

## 📂 **Project Structure**  
```
faceted-image-search
│-- README.md              # Project Documentation
│-- food_metadata.json      # JSON file with categorized food images
│-- summary.txt/            # Summary with the link to the Algolia interface
```

---

## ⚙️ **How to Run**  

### 1️⃣ **Clone the Repository**  
```sh
$ git clone https://github.com/yourusername/faceted-image-search.git
$ cd faceted-image-search
```

### 2️⃣ **Set up Algolia**  
✔ **Sign up** at [Algolia](https://www.algolia.com)  
✔ **Create an index** and upload `data/food_metadata.json`  
✔ **Configure searchable facets** for filtering  

### 3️⃣ **Launch the Search Interface**  
✔ Open `src/search_interface.html` in your browser.  

---

## 📄 **JSON Metadata Example**  
```json
{
  "image_url": "https://unsplash.com/photos/croissant-on-top-of-stainless-steel-tray-lE5O9DktAQY",
  "artist_name": "John Smith",
  "year": 2023,
  "meal_type": {
    "level1": "Breakfast",
    "level2": "Continental",
    "level3": "Croissant"
  },
  "cuisine": {
    "level1": "Continental",
    "level2": "Pastries"
  },
  "dietary_preference": {
    "level1": "Vegetarian",
    "level2": "Baked Goods",
    "level3": "Croissant"
  }
}
```


