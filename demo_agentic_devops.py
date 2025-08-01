#!/usr/bin/env python3
"""
Demo script for Agentic DevOps Human-on-the-Sidelines framework

This script demonstrates the autonomous agents in action with simulated data.
"""

import os
import sys
import json
from datetime import datetime

def demo_agent_capabilities():
    """Demonstrate the capabilities of each autonomous agent."""
    
    print("🤖 Agentic DevOps: Human-on-the-Sidelines Demo")
    print("=" * 60)
    print()
    
    # Simulate agent operations
    agents_demo = {
        "cicd_orchestration": {
            "name": "CI/CD Orchestration Agent",
            "status": "operational",
            "autonomous_actions": [
                "Triggered security scan for PR #123",
                "Automatically rolled back deployment due to 15% error rate",
                "Optimized pipeline execution order saving 8 minutes",
                "Scaled build resources based on queue length"
            ],
            "human_interventions": 0,
            "confidence_score": 0.94
        },
        "infrastructure_management": {
            "name": "Infrastructure Management Agent", 
            "status": "operational",
            "autonomous_actions": [
                "Scaled down 3 underutilized VMs (saving $150/month)",
                "Provisioned additional capacity for load spike",
                "Cleaned up 5 unused storage accounts",
                "Optimized network routing for 12% latency improvement"
            ],
            "human_interventions": 1,  # Cost approval required
            "confidence_score": 0.89
        },
        "incident_response": {
            "name": "Incident Response Agent",
            "status": "operational", 
            "autonomous_actions": [
                "Detected and resolved memory leak in user-service",
                "Automatically restarted failed API gateway",
                "Scaled database connection pool during peak traffic",
                "Blocked suspicious IP after failed login attempts"
            ],
            "human_interventions": 0,
            "confidence_score": 0.91
        },
        "code_quality": {
            "name": "Enhanced Code Quality Agent",
            "status": "operational",
            "autonomous_actions": [
                "Reviewed 8 PRs with security and quality feedback",
                "Blocked 2 PRs with critical security vulnerabilities", 
                "Suggested performance improvements for database queries",
                "Enforced coding standards across 15 commits"
            ],
            "human_interventions": 0,
            "confidence_score": 0.96
        },
        "cost_optimization": {
            "name": "Cost Optimization Agent",
            "status": "operational",
            "autonomous_actions": [
                "Identified $2,400 monthly savings opportunities",
                "Automatically shutdown dev environments overnight",
                "Recommended reserved instance purchases",
                "Optimized storage tiers for archival data"
            ],
            "human_interventions": 1,  # Budget approval needed
            "confidence_score": 0.88
        }
    }
    
    # Display agent status
    print("📊 Agent Status Summary")
    print("-" * 40)
    
    total_autonomous_actions = 0
    total_human_interventions = 0
    
    for agent_id, agent in agents_demo.items():
        status_emoji = "✅" if agent["status"] == "operational" else "❌"
        confidence_color = "🟢" if agent["confidence_score"] > 0.9 else "🟡" if agent["confidence_score"] > 0.8 else "🔴"
        
        print(f"{status_emoji} {agent['name']}")
        print(f"   Confidence: {confidence_color} {agent['confidence_score']:.0%}")
        print(f"   Autonomous Actions: {len(agent['autonomous_actions'])}")
        print(f"   Human Interventions: {agent['human_interventions']}")
        print()
        
        total_autonomous_actions += len(agent['autonomous_actions'])
        total_human_interventions += agent['human_interventions']
    
    # Summary metrics
    print("📈 Human-on-the-Sidelines Metrics")
    print("-" * 40)
    print(f"Total Autonomous Actions: {total_autonomous_actions}")
    print(f"Total Human Interventions: {total_human_interventions}")
    
    autonomous_rate = (total_autonomous_actions / (total_autonomous_actions + total_human_interventions)) * 100
    print(f"Autonomous Operation Rate: {autonomous_rate:.1f}%")
    print(f"Human Intervention Rate: {100 - autonomous_rate:.1f}%")
    print()
    
    # Recent autonomous actions
    print("🔄 Recent Autonomous Actions")
    print("-" * 40)
    
    for agent_id, agent in agents_demo.items():
        print(f"\n{agent['name']}:")
        for action in agent['autonomous_actions'][-2:]:  # Show last 2 actions
            print(f"  • {action}")
    
    print()
    print("🎯 Key Benefits Achieved:")
    print("  • 95%+ autonomous operation rate")
    print("  • Reduced MTTR from 45 minutes to 8 minutes")
    print("  • $3,000+ monthly cost savings identified")
    print("  • Zero production incidents caused by autonomous actions")
    print("  • Human team focused on strategic initiatives")
    print()
    
    # Future scope
    print("🚀 Future Scope")
    print("-" * 40)
    print("• Enhanced ML models for predictive failure detection")
    print("• Cross-cloud resource optimization") 
    print("• Automated security threat response")
    print("• Intelligent capacity planning")
    print("• Self-healing infrastructure capabilities")
    print()
    
    print("✨ The future of DevOps is autonomous, with humans providing")
    print("   strategic oversight and handling only exceptional cases.")

def demo_escalation_scenarios():
    """Demonstrate when agents escalate to humans."""
    
    print("\n🚨 Human Escalation Scenarios")
    print("=" * 60)
    
    escalation_examples = [
        {
            "agent": "Infrastructure Management Agent",
            "scenario": "Cost increase exceeds 20% threshold",
            "reason": "Proposed scaling would increase monthly costs by $5,000",
            "action": "Escalated to infrastructure lead for budget approval",
            "confidence": 0.95
        },
        {
            "agent": "Incident Response Agent", 
            "scenario": "Unknown incident pattern detected",
            "reason": "Never seen this type of database corruption before",
            "action": "Escalated to senior DBA with complete context",
            "confidence": 0.45
        },
        {
            "agent": "CI/CD Orchestration Agent",
            "scenario": "Critical production deployment",
            "reason": "High-impact deployment affecting payment system",
            "action": "Requires manual approval from tech lead",
            "confidence": 0.88
        }
    ]
    
    for i, scenario in enumerate(escalation_examples, 1):
        print(f"\n{i}. {scenario['scenario']}")
        print(f"   Agent: {scenario['agent']}")
        print(f"   Reason: {scenario['reason']}")
        print(f"   Action: {scenario['action']}")
        print(f"   Confidence: {scenario['confidence']:.0%}")
    
    print("\n💡 Smart escalation ensures human expertise is applied")
    print("   where it's most valuable while maintaining safety.")

if __name__ == "__main__":
    try:
        demo_agent_capabilities()
        demo_escalation_scenarios()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nError running demo: {e}")
        sys.exit(1)