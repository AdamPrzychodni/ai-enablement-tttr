def get_recommendations(category_scores):
    """Generates tailored recommendations for each category based on its score."""
    recommendations = {}
    for category, score in category_scores.items():
        recs = []
        if category == "Digital Infrastructure":
            if score <= 50:
                recs.append("Focus on centralizing data storage (e.g., Google Drive, SharePoint).")
                recs.append("Explore a CRM for managing stakeholder relationships.")
            else:
                recs.append("Investigate cloud services (AWS, Azure, GCP) for scalable infrastructure.")
        
        elif category == "Leadership & Culture":
            if score <= 50:
                recs.append("Share success stories of AI in other nonprofits with leadership.")
                recs.append("Organize a workshop on the basics of AI to demystify the technology.")
            else:
                recs.append("Develop a formal AI strategy that aligns with your organization's mission.")

        elif category == "Staff Capacity":
            if score <= 50:
                recs.append("Provide access to free online courses on data literacy (e.g., Coursera, edX).")
                recs.append("Identify 'digital champions' within the team to support colleagues.")
            else:
                recs.append("Create a formal professional development plan for AI-related skills.")

        elif category == "Data Readiness":
            if score <= 50:
                recs.append("Develop a simple data collection and management policy.")
                recs.append("Start a project to clean and consolidate your most critical dataset.")
            else:
                recs.append("Implement a formal data governance framework and ensure data security.")

        elif category == "Financial Resources":
            if score <= 50:
                recs.append("Research grants and funding opportunities specifically for digital transformation.")
                recs.append("Start with low-cost AI tools to demonstrate value before seeking a larger budget.")
            else:
                recs.append("Develop a multi-year technology roadmap with clear budget allocations.")

        elif category == "Use Case Clarity":
            if score <= 50:
                recs.append("Brainstorm a list of current challenges and bottlenecks in your daily operations.")
                recs.append("Define one small, specific problem that could be a good candidate for a pilot AI project.")
            else:
                recs.append("Create a detailed project plan for your top-priority AI use case.")

        recommendations[category] = recs
    return recommendations
