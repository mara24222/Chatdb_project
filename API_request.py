from openai import OpenAI

# API call to OpenAI — insert your API key
client = OpenAI(api_key="YOUR API KEY")

def ask_chatdb(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that only returns MySQL queries — no explanations, no markdown, no comments.\n\n"

                    "Use only these schemas:\n\n"

                    " Database: entertainment\n"
                    "- netflix_users(user_id, name, age, country)\n"
                    "- favorite_genre(user_id, favorite_genre)\n"
                    "- watch_time(user_id, watch_time_hours, last_login)\n"
                    "- subscriptions(user_id, subscription_type)\n\n"

                    " Database: GYM\n"
                    "- user_info(gym_id, gender, age)\n"
                    "- Time_in_Gym(gym_id, Avg_time_in, Avg_time_out)\n"
                    "- fitness_info(gym_id, fave_group_lesson)\n"
                    "- gym_info(gym_id, visits_per_week, membership_type)\n\n"

                    " Database: shopping\n"
                    "- customer_info(customer_id, name, gender, age, Prefered_payment, Frequency_Of_Purchases)\n"
                    "- purchase_info(customer_id, location, Item_Purchased, Category, Purchase_Amount, size, color, Review_Rating, Payment_Method, Shipping_Type, Discount_Applied, Promo_Code_Used)\n\n"

                    "Join rules:\n"
                    "- In entertainment, join tables using `user_id`\n"
                    "- In GYM, join using `gym_id`\n"
                    "- In shopping, join using `customer_id`\n"
                    "- Always use JOINs when data is from more than one table\n\n"

                    "Insert rules for new users in entertainment:\n"
                    "- Insert into `netflix_users` with: user_id, name, age, country\n"
                    "- Also insert into `favorite_genre` using the same user_id and genre\n"
                    "- Always generate both INSERT statements together\n"
                    "- Use user_id values like 9001, 9002, etc., if not given\n\n"

                    "Insert rules for GYM:\n"
                    "- Insert into `user_info` with: gym_id, gender, age\n"
                    "- Optionally insert into `fitness_info` and `gym_info` using the same gym_id\n"
                    "- Use gym_id values like 3001, 3002, etc., if not given\n\n"

                    "Insert rules for shopping:\n"
                    "- Insert into `customer_info` with: customer_id, name, gender, age, Prefered_payment, Frequency_Of_Purchases\n"
                    "- Optionally insert into `purchase_info` using the same customer_id\n"
                    "- Use customer_id values like 7001, 7002, etc., if not given\n\n"

                    "You can also handle UPDATE and DELETE statements for all tables across all databases.\n"
                    "Only return valid SQL that can be executed."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )

    raw_output = response.choices[0].message.content.strip()

    # Remove markdown formatting
    if "```" in raw_output:
        raw_output = raw_output.split("```")[1]
    if raw_output.strip().lower().startswith("sql"):
        raw_output = raw_output.strip()[3:]

    # Remove any accidental non-SQL lines (safety)
    lines = raw_output.splitlines()
    only_sql = "\n".join([line for line in lines if not line.lower().startswith("the ")])

    return only_sql.strip()

