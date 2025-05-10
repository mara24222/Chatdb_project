import mysql.connector
 
#this funtion helps detect which database chagtpt needs to use based on some key words, may need some work, espciallt for shopping wrong words. 

def detect_database(question):
    q = question.lower()
    
    if any(word in q for word in ["netflix", "watch", "show", "movie", "series", "subscription", "plan", "genre", "streaming"]):
        return "entertainment"
    elif any(word in q for word in ["gym", "fitness", "workout", "trainer", "membership", "visits", "exercise", "group class"]):
        return "GYM"
    elif any(word in q for word in ["shopping", "purchase", "order", "cart", "product", "item", "customer", "store", "receipt"]):
        return "shopping"
    else:
        return "entertainment"