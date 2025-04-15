# **Faceted Image Search: Food Photography Collection**   
---

## **Overview**  
This project showcases the design and implementation of faceted search and metadata-driven navigation for a food photography collection.

The system enables users to efficiently browse, search, and filter food images based on meal type, cuisine, and dietary preference using Algolia’s faceted search. The project demonstrates how structured metadata enhances searchability and improves user experience. 

---

## **Project Goal**  
The goal of this project is to create a structured **image search experience** optimized for **food lovers, bloggers, chefs, and marketers**.  
By implementing a **hierarchical faceted classification**, users can explore food images with **multiple levels of categorization**.  

### **Why This Matters for Product Management**  
- **Design user-friendly search experiences** using metadata and taxonomy.  
- **Structure large datasets** into logical hierarchies for better UX.  
- **Work with Algolia and JSON data** for scalable search solutions.  
- **Apply product thinking** by optimizing navigation for target users.  

---

## **Features**  
- **Faceted Search**: Users can navigate images using structured facets such as:  
   - **Meal Type**: Breakfast, Lunch, Dinner  
- **Hierarchical Metadata**: Three-level categorization for refined search results.  
- **JSON Metadata Format**: Organized dataset for easy scalability and search integration.  
- **Algolia Integration**: Hosted search interface powered by **Algolia** for fast, user-friendly searching.  

---

## **Project Structure**  
```
faceted-image-search
│-- README.md              # Project Documentation
│-- food_metadata.json      # JSON file with categorized food images
│-- summary.txt/            # Summary with the link to the Algolia interface
```

---

## **How to Run**  

### 1️ **Clone the Repository**  
```sh
$ git clone https://github.com/heyaigerim/my-projects/tree/main/Faceted%20Image%20Search
$ cd faceted-image-search
```

### 2️ **Set up Algolia**  
1. **Sign up** at [Algolia](https://www.algolia.com)  
2. **Create an index** and upload `data/food_metadata.json`  
3. **Configure searchable facets** for filtering  

### 3️ **Launch the Search Interface**  
✔ Open `src/search_interface.html` in your browser.  

---

## **JSON Metadata Example**  
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
## Future Enhancements
This project lays the foundation for a scalable and user-friendly search experience. Future iterations could include:
- Personalized recommendations based on user interactions.
- Advanced filtering options such as ingredient-based searches.
- Integration with external APIs for dynamic food photography datasets.
- AI-powered tagging to enhance metadata enrichment.
- This project not only demonstrates technical execution but also product-driven decision-making in creating an optimized search experience for diverse user needs.

