"""
Farmer Training Module Generator
AI-Powered Agricultural Advisory System
"""

from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)


class AgricultureExpert:
    """Contains farming knowledge for common crops and problems"""
    
    # Farming knowledge database
    CROP_INFO = {
        "rice": {
            "name": "Rice",
            "season": "Kharif (June to October)",
            "water": "Needs standing water, 5-7 cm depth",
            "spacing": "20 cm between plants, 20 cm between rows",
            "duration": "120-150 days from sowing to harvest"
        },
        "wheat": {
            "name": "Wheat", 
            "season": "Rabi (November to March)",
            "water": "4-6 irrigations, avoid waterlogging",
            "spacing": "5 cm between plants, 22 cm between rows",
            "duration": "110-130 days"
        },
        "tomato": {
            "name": "Tomato",
            "season": "Year-round with care",
            "water": "Regular watering, avoid wet leaves",
            "spacing": "45 cm between plants, 60 cm between rows", 
            "duration": "90-120 days"
        }
    }
    
    PROBLEM_SOLUTIONS = {
        "irrigation": {
            "key_techniques": ["Drip irrigation", "Sprinkler systems", "Rainwater harvesting"],
            "steps": [
                "Measure soil moisture regularly",
                "Water at plant roots, not leaves",
                "Water early morning or evening",
                "Adjust based on weather conditions"
            ],
            "benefits": "Saves 30-50% water, increases yield by 20-30%"
        },
        "pest control": {
            "key_techniques": ["Integrated Pest Management", "Neem oil spray", "Companion planting"],
            "steps": [
                "Regular field inspection",
                "Identify pest type correctly",
                "Use natural predators first",
                "Apply chemicals only if needed"
            ],
            "benefits": "Reduces chemical use by 40-60%, protects beneficial insects"
        },
        "soil health": {
            "key_techniques": ["Organic compost", "Crop rotation", "Green manure"],
            "steps": [
                "Test soil every season",
                "Add organic matter regularly",
                "Maintain proper pH level",
                "Avoid soil compaction"
            ],
            "benefits": "Improves yield by 25-40%, reduces fertilizer need"
        }
    }
    
    @staticmethod
    def get_crop_details(crop_name):
        """Get information about a specific crop"""
        crop_lower = crop_name.lower()
        if crop_lower in AgricultureExpert.CROP_INFO:
            return AgricultureExpert.CROP_INFO[crop_lower]
        else:
            return {
                "name": crop_name.title(),
                "season": "Adapt to local season",
                "water": "Based on local conditions",
                "spacing": "Follow seed packet instructions",
                "duration": "Varies by variety"
            }
    
    @staticmethod
    def get_problem_solution(problem_name):
        """Get solutions for a specific problem"""
        problem_lower = problem_name.lower()
        if problem_lower in AgricultureExpert.PROBLEM_SOLUTIONS:
            return AgricultureExpert.PROBLEM_SOLUTIONS[problem_lower]
        else:
            return {
                "key_techniques": ["Integrated approach", "Regular monitoring"],
                "steps": ["Assess situation", "Plan solution", "Implement carefully"],
                "benefits": "Improved crop health and yield"
            }


class AISystem:
    """Manages AI-related functionality"""
    
    @staticmethod
    def generate_ai_insight(crop, region, problem):
        """
        Simulate AI generation
        In a full system, this would call a real AI model
        """
        # This simulates what an AI might generate
        insights = [
            f"AI analysis suggests focusing on {region}-specific adaptation for {crop}.",
            f"Machine learning models indicate integrated approach works best for {problem}.",
            f"Data patterns show {crop} responds well to timely {problem} management.",
            f"AI recommendation: Combine traditional knowledge with modern techniques."
        ]
        
        # Return different insights based on input (simple simulation)
        input_hash = hash(f"{crop}{region}{problem}") % len(insights)
        return insights[input_hash]
    
    @staticmethod
    def check_ai_availability():
        """
        Check if AI model is available
        Returns True if AI is working, False otherwise
        """
        # In a real system, this would check if the AI model is loaded
        # For this demo, we simulate that AI is available
        return True


class TrainingModuleBuilder:
    """Builds complete training modules"""
    
    @staticmethod
    def create_module(crop, region, problem, language="English"):
        """Create a complete training module"""
        
        # Get current time for the module
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d %B %Y, %I:%M %p")
        
        # Get farming knowledge
        crop_info = AgricultureExpert.get_crop_details(crop)
        problem_solution = AgricultureExpert.get_problem_solution(problem)
        
        # Get AI insight if available
        ai_available = AISystem.check_ai_availability()
        ai_insight = ""
        if ai_available:
            ai_insight = AISystem.generate_ai_insight(crop, region, problem)
        
        # Build the module content
        module_content = f"""
# FARMER TRAINING MODULE
## Crop: {crop_info['name']} | Region: {region} | Language: {language}

### 📅 GENERATED ON: {formatted_time}

---

## 🌾 ABOUT THIS CROP

**Crop Name:** {crop_info['name']}
**Best Season:** {crop_info['season']}
**Water Needs:** {crop_info['water']}
**Plant Spacing:** {crop_info['spacing']}
**Growth Duration:** {crop_info['duration']}

---

## 🎯 FOCUS AREA: {problem.upper()}

### AI-GENERATED INSIGHT:
{ai_insight if ai_insight else "System analysis recommends integrated management approach."}

### RECOMMENDED TECHNIQUES:
{' • '.join(problem_solution['key_techniques'])}

### STEP-BY-STEP GUIDE:

1. **Week 1-2: Assessment & Planning**
   - Evaluate current {problem} conditions
   - Gather necessary tools and resources
   - Create implementation schedule

2. **Week 3-8: Implementation**
   {chr(10).join('   - ' + step for step in problem_solution['steps'])}
   - Monitor progress weekly
   - Make adjustments as needed

3. **Week 9-12: Evaluation**
   - Measure results and improvements
   - Document lessons learned
   - Share knowledge with other farmers

### KEY BENEFITS:
{problem_solution['benefits']}

### REGION-SPECIFIC ADVICE FOR {region.upper()}:
- Consider local weather patterns
- Adapt to soil conditions in your area
- Consult local agriculture department
- Join local farmer groups for support

---

## 📊 EXPECTED RESULTS

### QUANTITATIVE IMPROVEMENTS:
- {problem} management: 40-60% better
- Crop yield increase: 20-35%
- Input cost reduction: 15-25%
- Labor efficiency: 20-30% improvement

### QUALITATIVE BENEFITS:
- Healthier crops
- Better soil quality
- More sustainable farming
- Increased confidence in farming

---

## 🛠️ IMPLEMENTATION TIPS

### DO'S:
✓ Start with small pilot area
✓ Keep detailed records
✓ Monitor daily progress
✓ Seek expert advice when needed
✓ Share results with community

### DON'TS:
✗ Don't implement everything at once
✗ Don't ignore warning signs
✗ Don't skip monitoring
✗ Don't work in isolation
✗ Don't forget to document

---

## ❓ FREQUENTLY ASKED QUESTIONS

**Q: How long before I see results?**
A: Most farmers see improvements within 4-6 weeks.

**Q: What if it doesn't work for my farm?**
A: Adjust the approach based on your specific conditions and consult local experts.

**Q: Is this expensive to implement?**
A: Many techniques are low-cost, and the yield increase usually covers any costs.

**Q: Can I use this with other crops?**
A: Yes, adapt the principles to other crops you grow.

---

## 🔧 SYSTEM INFORMATION

### TECHNOLOGY USED:
- Web Application: Flask Python Framework
- Knowledge Base: Agricultural Expert System
- AI Integration: Generative AI System Architecture
- Interface: Responsive Web Design

### GENERATION DETAILS:
- Module Created: {formatted_time}
- AI Assistance: {'Available' if ai_available else 'Not available'}
- Content Type: Personalized farming guidance
- System Status: Operational

---

## 📞 GETTING HELP

### LOCAL RESOURCES:
- Contact {region} Agriculture Department
- Visit nearest Krishi Vigyan Kendra (KVK)
- Join farmer WhatsApp groups
- Attend local farming workshops

### DIGITAL TOOLS:
- Use weather forecast apps
- Try soil testing mobile apps
- Watch farming tutorial videos
- Join online farmer communities

---
*This training module was generated automatically based on agricultural best practices.*
*Always consult local agricultural experts before implementing new techniques.*
"""
        
        return {
            "content": module_content.strip(),
            "metadata": {
                "generation_time": formatted_time,
                "crop": crop,
                "region": region,
                "problem": problem,
                "language": language,
                "ai_used": ai_available
            }
        }


# Web Application Routes
@app.route('/')
def show_homepage():
    """Display the main web page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_training_module():
    """Create and return a training module"""
    
    try:
        # Get data from the web form
        request_data = request.get_json()
        
        # Extract the information
        crop_type = request_data.get('crop', '').strip()
        region_name = request_data.get('region', '').strip()
        problem_type = request_data.get('problem', '').strip()
        language_pref = request_data.get('language', 'English')
        
        # Check if all required fields are filled
        if not crop_type or not region_name or not problem_type:
            return jsonify({
                "success": False,
                "error": "Please fill in all fields: Crop, Region, and Problem"
            }), 400
        
        # Print to console for debugging
        print(f"\nCreating training module for:")
        print(f"  Crop: {crop_type}")
        print(f"  Region: {region_name}")
        print(f"  Problem: {problem_type}")
        print(f"  Language: {language_pref}")
        
        # Build the training module
        module_data = TrainingModuleBuilder.create_module(
            crop_type, region_name, problem_type, language_pref
        )
        
        # Prepare the response
        response_data = {
            "success": True,
            "data": {
                "title": f"{crop_type.title()} Farming Training Module",
                "subtitle": f"Region: {region_name} | Focus: {problem_type.title()}",
                "content": module_data["content"],
                "language": language_pref
            },
            "system_info": {
                "generated_at": module_data["metadata"]["generation_time"],
                "ai_assistance": module_data["metadata"]["ai_used"]
            }
        }
        
        return jsonify(response_data)
        
    except Exception as error:
        # Handle any errors
        print(f"Error creating module: {error}")
        return jsonify({
            "success": False,
            "error": "Could not generate training module. Please try again."
        }), 500


@app.route('/health', methods=['GET'])
def check_health():
    """Check if the system is working"""
    return jsonify({
        "status": "working",
        "service": "farmer_training_generator",
        "time": datetime.now().isoformat()
    })


# Start the application
if __name__ == '__main__':
    
    # Show startup message
    print("\n" + "=" * 60)
    print("FARMER TRAINING MODULE GENERATOR")
    print("=" * 60)
    print("Starting web server...")
    print(f"Local website: http://127.0.0.1:5000")
    print(f"Health check: http://127.0.0.1:5000/health")
    print("=" * 60)
    print("\nReady to generate training modules!")
    print("Open the website in your browser to begin.")
    print("\n" + "=" * 60)
    
    # Run the web server
    app.run(
        host='0.0.0.0',  # Allow connections from any device on network
        port=5000,        # Use port 5000
        debug=True        # Show detailed errors for development
    )
