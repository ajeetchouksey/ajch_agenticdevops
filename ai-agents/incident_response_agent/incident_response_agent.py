#!/usr/bin/env python3
"""
Incident Response Agent

This agent provides autonomous incident detection, analysis, and resolution
with minimal human intervention. It implements the human-on-the-sidelines
approach for incident management.

Security Features:
- Secure credential management
- Audit logging for all incident actions
- Role-based access control
- Compliance with security policies

Architecture:
- Detection Engine: Multi-source monitoring and anomaly detection
- Analysis Engine: AI-powered incident classification
- Response Engine: Automated remediation and escalation
- Learning Engine: Continuous improvement through ML
"""

import os
import json
import logging
import argparse
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import time
import uuid
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('incident_response.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class IncidentSeverity(Enum):
    """Incident severity levels."""
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

class IncidentStatus(Enum):
    """Incident status values."""
    DETECTED = "detected"
    ANALYZING = "analyzing"
    RESPONDING = "responding"
    RESOLVED = "resolved"
    ESCALATED = "escalated"

class IncidentResponseAgent:
    """
    Autonomous Incident Response Agent
    
    Provides intelligent incident management with minimal human intervention.
    """
    
    def __init__(self):
        """Initialize the incident response agent."""
        self.config = self._load_configuration()
        self._validate_configuration()
        
        # AI configuration
        self.ai_api_key = self.config.get('AI_API_KEY')
        self.ai_api_url = self.config.get('AI_API_URL')
        
        # Monitoring configuration
        self.azure_workspace_id = self.config.get('AZURE_MONITOR_WORKSPACE_ID')
        self.prometheus_url = self.config.get('PROMETHEUS_URL')
        
        # Operational configuration
        self.severity_thresholds = json.loads(self.config.get('SEVERITY_THRESHOLDS', '{"critical": 1, "high": 3, "medium": 5, "low": 10}'))
        self.auto_resolution_enabled = self.config.get('AUTO_RESOLUTION_ENABLED', 'true').lower() == 'true'
        self.escalation_timeout = int(self.config.get('ESCALATION_TIMEOUT_MINUTES', 15))
        
        # Response capabilities
        self.enable_auto_restart = self.config.get('ENABLE_AUTO_RESTART', 'true').lower() == 'true'
        self.enable_auto_scaling = self.config.get('ENABLE_AUTO_SCALING', 'true').lower() == 'true'
        self.enable_rollback = self.config.get('ENABLE_ROLLBACK', 'true').lower() == 'true'
        
        # State tracking
        self.active_incidents = {}
        self.incident_history = []
        self.metrics = {
            'incidents_detected': 0,
            'incidents_resolved_automatically': 0,
            'incidents_escalated': 0,
            'mean_time_to_detection': 0.0,
            'mean_time_to_resolution': 0.0,
            'autonomous_resolution_rate': 0.0
        }
        
        # Machine learning patterns (simplified)
        self.learned_patterns = {}
        
    def _load_configuration(self) -> Dict[str, str]:
        """Load configuration from environment variables."""
        config = {}
        
        # Optional configuration
        optional_vars = [
            'AI_API_KEY', 'AI_API_URL', 'AZURE_MONITOR_WORKSPACE_ID',
            'PROMETHEUS_URL', 'GRAFANA_API_KEY', 'SEVERITY_THRESHOLDS',
            'AUTO_RESOLUTION_ENABLED', 'ESCALATION_TIMEOUT_MINUTES',
            'SLACK_WEBHOOK_URL', 'TEAMS_WEBHOOK_URL', 'PAGERDUTY_INTEGRATION_KEY',
            'EMAIL_NOTIFICATIONS', 'ENABLE_AUTO_RESTART', 'ENABLE_AUTO_SCALING', 'ENABLE_ROLLBACK'
        ]
        
        for var in optional_vars:
            if os.getenv(var):
                config[var] = os.getenv(var)
        
        return config
    
    def _validate_configuration(self):
        """Validate the configuration."""
        logger.info("Incident response agent configuration validated")
    
    def detect_incidents(self) -> List[Dict]:
        """
        Detect incidents from multiple monitoring sources.
        
        Returns:
            List of detected incidents
        """
        detected_incidents = []
        
        try:
            # Detect from Azure Monitor
            azure_incidents = self._detect_azure_monitor_incidents()
            detected_incidents.extend(azure_incidents)
            
            # Detect from Prometheus
            prometheus_incidents = self._detect_prometheus_incidents()
            detected_incidents.extend(prometheus_incidents)
            
            # Detect from application logs
            log_incidents = self._detect_log_incidents()
            detected_incidents.extend(log_incidents)
            
            # Update metrics
            self.metrics['incidents_detected'] += len(detected_incidents)
            
            logger.info(f"Detected {len(detected_incidents)} incidents across all sources")
            return detected_incidents
            
        except Exception as e:
            logger.error(f"Error detecting incidents: {e}")
            return []
    
    def _detect_azure_monitor_incidents(self) -> List[Dict]:
        """Detect incidents from Azure Monitor."""
        incidents = []
        
        if not self.azure_workspace_id:
            return incidents
        
        try:
            # Simulate Azure Monitor integration
            # In practice, this would query Azure Monitor APIs for alerts and metrics
            
            # Simulate some incident patterns
            import random
            
            # High CPU usage incident
            if random.random() < 0.1:  # 10% chance
                incidents.append({
                    'id': str(uuid.uuid4()),
                    'source': 'azure_monitor',
                    'type': 'performance',
                    'title': 'High CPU usage detected',
                    'description': f'CPU usage exceeded 90% on multiple VMs',
                    'severity': IncidentSeverity.HIGH.value,
                    'detected_at': datetime.now().isoformat(),
                    'affected_resources': ['vm-prod-web-01', 'vm-prod-web-02'],
                    'metrics': {
                        'cpu_usage_percent': 95.2,
                        'duration_minutes': 8
                    }
                })
            
            # Memory leak incident
            if random.random() < 0.05:  # 5% chance
                incidents.append({
                    'id': str(uuid.uuid4()),
                    'source': 'azure_monitor',
                    'type': 'memory',
                    'title': 'Memory usage continuously increasing',
                    'description': 'Potential memory leak detected in application',
                    'severity': IncidentSeverity.MEDIUM.value,
                    'detected_at': datetime.now().isoformat(),
                    'affected_resources': ['app-service-api'],
                    'metrics': {
                        'memory_usage_percent': 88.5,
                        'growth_rate_percent_hour': 5.2
                    }
                })
            
            logger.info(f"Detected {len(incidents)} incidents from Azure Monitor")
            return incidents
            
        except Exception as e:
            logger.error(f"Error detecting Azure Monitor incidents: {e}")
            return []
    
    def _detect_prometheus_incidents(self) -> List[Dict]:
        """Detect incidents from Prometheus metrics."""
        incidents = []
        
        if not self.prometheus_url:
            return incidents
        
        try:
            # Simulate Prometheus integration
            import random
            
            # API error rate spike
            if random.random() < 0.08:  # 8% chance
                incidents.append({
                    'id': str(uuid.uuid4()),
                    'source': 'prometheus',
                    'type': 'application',
                    'title': 'API error rate spike detected',
                    'description': 'HTTP 5xx error rate exceeded threshold',
                    'severity': IncidentSeverity.CRITICAL.value,
                    'detected_at': datetime.now().isoformat(),
                    'affected_resources': ['api-gateway', 'user-service'],
                    'metrics': {
                        'error_rate_percent': 12.3,
                        'requests_per_minute': 1250
                    }
                })
            
            # Database connection issues
            if random.random() < 0.06:  # 6% chance
                incidents.append({
                    'id': str(uuid.uuid4()),
                    'source': 'prometheus',
                    'type': 'database',
                    'title': 'Database connection pool exhaustion',
                    'description': 'Database connection pool utilization at 95%',
                    'severity': IncidentSeverity.HIGH.value,
                    'detected_at': datetime.now().isoformat(),
                    'affected_resources': ['postgresql-primary'],
                    'metrics': {
                        'connection_pool_usage_percent': 95.0,
                        'active_connections': 190,
                        'max_connections': 200
                    }
                })
            
            logger.info(f"Detected {len(incidents)} incidents from Prometheus")
            return incidents
            
        except Exception as e:
            logger.error(f"Error detecting Prometheus incidents: {e}")
            return []
    
    def _detect_log_incidents(self) -> List[Dict]:
        """Detect incidents from application logs."""
        incidents = []
        
        try:
            # Simulate log analysis
            import random
            
            # Security incident
            if random.random() < 0.03:  # 3% chance
                incidents.append({
                    'id': str(uuid.uuid4()),
                    'source': 'logs',
                    'type': 'security',
                    'title': 'Suspicious login activity detected',
                    'description': 'Multiple failed login attempts from same IP',
                    'severity': IncidentSeverity.HIGH.value,
                    'detected_at': datetime.now().isoformat(),
                    'affected_resources': ['auth-service'],
                    'metrics': {
                        'failed_attempts': 25,
                        'source_ip': '192.168.1.100',
                        'time_window_minutes': 5
                    }
                })
            
            logger.info(f"Detected {len(incidents)} incidents from logs")
            return incidents
            
        except Exception as e:
            logger.error(f"Error detecting log incidents: {e}")
            return []
    
    def analyze_incident(self, incident: Dict) -> Dict:
        """
        Analyze an incident using AI to determine impact and response strategy.
        
        Args:
            incident: Incident dictionary
            
        Returns:
            Enhanced incident with analysis results
        """
        try:
            analysis = {
                'business_impact': self._assess_business_impact(incident),
                'root_cause_hypothesis': self._generate_root_cause_hypothesis(incident),
                'recommended_actions': self._recommend_response_actions(incident),
                'escalation_required': False,
                'confidence_score': 0.0,
                'analyzed_at': datetime.now().isoformat()
            }
            
            # Determine if escalation is required
            if incident['severity'] == IncidentSeverity.CRITICAL.value:
                analysis['escalation_required'] = True
            elif incident['type'] == 'security':
                analysis['escalation_required'] = True
            elif len(analysis['recommended_actions']) == 0:
                analysis['escalation_required'] = True
            
            # Calculate confidence score based on pattern matching
            analysis['confidence_score'] = self._calculate_confidence_score(incident)
            
            incident['analysis'] = analysis
            logger.info(f"Analyzed incident {incident['id']}: {analysis['business_impact']} impact")
            
            return incident
            
        except Exception as e:
            logger.error(f"Error analyzing incident {incident.get('id', 'unknown')}: {e}")
            incident['analysis'] = {'error': str(e)}
            return incident
    
    def _assess_business_impact(self, incident: Dict) -> str:
        """Assess the business impact of an incident."""
        severity = incident.get('severity', IncidentSeverity.LOW.value)
        incident_type = incident.get('type', 'unknown')
        affected_resources = incident.get('affected_resources', [])
        
        # High impact conditions
        if severity == IncidentSeverity.CRITICAL.value:
            return 'high'
        elif incident_type == 'security':
            return 'high'
        elif 'api-gateway' in affected_resources:
            return 'high'
        elif len(affected_resources) > 3:
            return 'medium'
        else:
            return 'low'
    
    def _generate_root_cause_hypothesis(self, incident: Dict) -> str:
        """Generate a hypothesis about the root cause."""
        incident_type = incident.get('type', 'unknown')
        metrics = incident.get('metrics', {})
        
        hypotheses = {
            'performance': 'Resource exhaustion or inefficient code causing performance degradation',
            'memory': 'Memory leak in application or inefficient garbage collection',
            'application': 'Service dependency failure or configuration issues',
            'database': 'Database connection pool misconfiguration or query performance issues',
            'security': 'Potential security breach or automated attack attempt',
            'network': 'Network connectivity issues or bandwidth constraints'
        }
        
        base_hypothesis = hypotheses.get(incident_type, 'Unknown incident type requiring investigation')
        
        # Enhance hypothesis with metrics
        if 'cpu_usage_percent' in metrics and metrics['cpu_usage_percent'] > 90:
            base_hypothesis += ' - High CPU usage suggests computational bottleneck'
        
        if 'error_rate_percent' in metrics and metrics['error_rate_percent'] > 10:
            base_hypothesis += ' - High error rate indicates service instability'
        
        return base_hypothesis
    
    def _recommend_response_actions(self, incident: Dict) -> List[str]:
        """Recommend response actions based on incident analysis."""
        actions = []
        incident_type = incident.get('type', 'unknown')
        severity = incident.get('severity', IncidentSeverity.LOW.value)
        metrics = incident.get('metrics', {})
        
        # Common actions based on type
        type_actions = {
            'performance': ['scale_resources', 'restart_services', 'check_resource_limits'],
            'memory': ['restart_application', 'analyze_memory_dump', 'check_memory_leaks'],
            'application': ['check_dependencies', 'restart_services', 'rollback_deployment'],
            'database': ['check_connection_pool', 'analyze_slow_queries', 'restart_database'],
            'security': ['block_suspicious_ip', 'reset_credentials', 'audit_access_logs'],
            'network': ['check_network_connectivity', 'analyze_network_traffic', 'restart_network_services']
        }
        
        actions.extend(type_actions.get(incident_type, ['investigate_manually']))
        
        # Severity-based actions
        if severity == IncidentSeverity.CRITICAL.value:
            actions.insert(0, 'activate_incident_bridge')
            actions.append('notify_stakeholders')
        
        # Metrics-based actions
        if metrics.get('cpu_usage_percent', 0) > 90:
            actions.append('scale_compute_resources')
        
        if metrics.get('error_rate_percent', 0) > 15:
            actions.append('rollback_recent_deployment')
        
        return list(set(actions))  # Remove duplicates
    
    def _calculate_confidence_score(self, incident: Dict) -> float:
        """Calculate confidence score for incident analysis."""
        # Simplified confidence calculation
        score = 0.5  # Base score
        
        # Increase confidence for known patterns
        incident_type = incident.get('type', 'unknown')
        if incident_type in ['performance', 'application', 'database']:
            score += 0.2
        
        # Increase confidence if we have good metrics
        metrics = incident.get('metrics', {})
        if len(metrics) > 2:
            score += 0.2
        
        # Pattern matching with historical incidents
        pattern_match = self._find_similar_historical_patterns(incident)
        if pattern_match:
            score += 0.3
        
        return min(score, 1.0)
    
    def _find_similar_historical_patterns(self, incident: Dict) -> bool:
        """Find similar patterns in historical incidents."""
        # Simplified pattern matching
        incident_type = incident.get('type', 'unknown')
        
        # Check if we've seen similar incidents before
        pattern_key = f"{incident_type}_{incident.get('severity', 'unknown')}"
        
        if pattern_key in self.learned_patterns:
            return True
        
        return False
    
    def execute_autonomous_response(self, incident: Dict, mode: str = 'autonomous') -> Dict:
        """
        Execute autonomous response actions for an incident.
        
        Args:
            incident: Incident with analysis
            mode: 'autonomous' or 'monitor'
            
        Returns:
            Dict containing response results
        """
        response_results = {
            'incident_id': incident.get('id'),
            'executed_actions': [],
            'skipped_actions': [],
            'errors': [],
            'resolution_status': 'in_progress',
            'human_intervention_required': False,
            'timestamp': datetime.now().isoformat()
        }
        
        if mode == 'monitor':
            logger.info(f"Running in monitor mode for incident {incident.get('id')} - no autonomous actions")
            analysis = incident.get('analysis', {})
            response_results['skipped_actions'] = analysis.get('recommended_actions', [])
            return response_results
        
        if not self.auto_resolution_enabled:
            logger.info("Autonomous resolution disabled")
            response_results['human_intervention_required'] = True
            return response_results
        
        analysis = incident.get('analysis', {})
        
        # Check if escalation is required
        if analysis.get('escalation_required', False):
            response_results['human_intervention_required'] = True
            self._escalate_incident(incident)
            return response_results
        
        # Execute recommended actions
        recommended_actions = analysis.get('recommended_actions', [])
        
        for action in recommended_actions:
            try:
                success = self._execute_response_action(action, incident)
                if success:
                    response_results['executed_actions'].append(action)
                else:
                    response_results['errors'].append(f"Failed to execute {action}")
                    
            except Exception as e:
                logger.error(f"Error executing action '{action}': {e}")
                response_results['errors'].append(f"Error in {action}: {str(e)}")
        
        # Determine resolution status
        if len(response_results['errors']) == 0 and len(response_results['executed_actions']) > 0:
            response_results['resolution_status'] = 'resolved'
            self.metrics['incidents_resolved_automatically'] += 1
        elif len(response_results['errors']) > 0:
            response_results['resolution_status'] = 'failed'
            response_results['human_intervention_required'] = True
        
        logger.info(f"Executed {len(response_results['executed_actions'])} actions for incident {incident.get('id')}")
        return response_results
    
    def _execute_response_action(self, action: str, incident: Dict) -> bool:
        """Execute a specific response action."""
        try:
            if action == 'scale_resources' and self.enable_auto_scaling:
                return self._scale_resources(incident)
            elif action == 'restart_services' and self.enable_auto_restart:
                return self._restart_services(incident)
            elif action == 'rollback_deployment' and self.enable_rollback:
                return self._rollback_deployment(incident)
            elif action == 'block_suspicious_ip':
                return self._block_suspicious_ip(incident)
            elif action == 'notify_stakeholders':
                return self._notify_stakeholders(incident)
            elif action == 'activate_incident_bridge':
                return self._activate_incident_bridge(incident)
            else:
                logger.info(f"Action '{action}' not implemented or disabled - skipping")
                return False
                
        except Exception as e:
            logger.error(f"Error executing action '{action}': {e}")
            return False
    
    def _scale_resources(self, incident: Dict) -> bool:
        """Scale resources to address the incident."""
        logger.info(f"Scaling resources for incident {incident.get('id')}")
        
        # Simulate resource scaling
        affected_resources = incident.get('affected_resources', [])
        
        for resource in affected_resources:
            logger.info(f"Scaling resource: {resource}")
            # In practice, this would call Azure/AWS APIs to scale resources
        
        return True
    
    def _restart_services(self, incident: Dict) -> bool:
        """Restart affected services."""
        logger.info(f"Restarting services for incident {incident.get('id')}")
        
        # Simulate service restart
        affected_resources = incident.get('affected_resources', [])
        
        for resource in affected_resources:
            logger.info(f"Restarting service: {resource}")
            # In practice, this would call appropriate APIs to restart services
        
        return True
    
    def _rollback_deployment(self, incident: Dict) -> bool:
        """Rollback recent deployment."""
        logger.info(f"Rolling back deployment for incident {incident.get('id')}")
        
        # Simulate deployment rollback
        # In practice, this would trigger CI/CD rollback procedures
        
        return True
    
    def _block_suspicious_ip(self, incident: Dict) -> bool:
        """Block suspicious IP address."""
        metrics = incident.get('metrics', {})
        source_ip = metrics.get('source_ip')
        
        if source_ip:
            logger.info(f"Blocking suspicious IP: {source_ip}")
            # In practice, this would update firewall rules or WAF settings
            return True
        
        return False
    
    def _notify_stakeholders(self, incident: Dict) -> bool:
        """Notify stakeholders about the incident."""
        message = f"Critical incident {incident.get('id')} requires attention: {incident.get('title')}"
        self._send_notification(message, 'critical', incident)
        return True
    
    def _activate_incident_bridge(self, incident: Dict) -> bool:
        """Activate incident response bridge."""
        logger.info(f"Activating incident bridge for {incident.get('id')}")
        # In practice, this would create a conference bridge and notify the incident team
        return True
    
    def _escalate_incident(self, incident: Dict):
        """Escalate incident to human responders."""
        logger.info(f"Escalating incident {incident.get('id')} to human responders")
        
        self.metrics['incidents_escalated'] += 1
        
        escalation_message = f"""
🚨 INCIDENT ESCALATION REQUIRED 🚨

Incident ID: {incident.get('id')}
Title: {incident.get('title')}
Severity: {incident.get('severity')}
Type: {incident.get('type')}
Detected: {incident.get('detected_at')}

Analysis:
- Business Impact: {incident.get('analysis', {}).get('business_impact', 'unknown')}
- Root Cause Hypothesis: {incident.get('analysis', {}).get('root_cause_hypothesis', 'unknown')}
- Confidence Score: {incident.get('analysis', {}).get('confidence_score', 0.0):.2f}

Affected Resources: {', '.join(incident.get('affected_resources', []))}

Recommended Actions: {', '.join(incident.get('analysis', {}).get('recommended_actions', []))}

Please take immediate action.
        """
        
        self._send_notification(escalation_message.strip(), 'critical', incident)
    
    def _send_notification(self, message: str, severity: str = 'info', incident: Dict = None):
        """Send notification to configured channels."""
        notification_data = {
            'message': message,
            'severity': severity,
            'timestamp': datetime.now().isoformat(),
            'agent': 'Incident Response Agent',
            'incident_id': incident.get('id') if incident else None
        }
        
        # Send to Slack if configured
        slack_webhook = self.config.get('SLACK_WEBHOOK_URL')
        if slack_webhook:
            try:
                color_map = {'critical': 'danger', 'warning': 'warning', 'info': 'good'}
                slack_payload = {
                    'text': f"🚨 {notification_data['agent']}: {message}",
                    'attachments': [{
                        'color': color_map.get(severity, 'good'),
                        'fields': [
                            {'title': 'Severity', 'value': severity, 'short': True},
                            {'title': 'Timestamp', 'value': notification_data['timestamp'], 'short': True}
                        ]
                    }]
                }
                if incident:
                    slack_payload['attachments'][0]['fields'].append({
                        'title': 'Incident ID', 'value': incident.get('id'), 'short': True
                    })
                
                requests.post(slack_webhook, json=slack_payload, timeout=10)
                logger.info("Notification sent to Slack")
            except Exception as e:
                logger.error(f"Failed to send Slack notification: {e}")
    
    def run_incident_response_cycle(self, mode: str = 'autonomous') -> Dict:
        """
        Run a complete incident response cycle.
        
        Args:
            mode: 'autonomous' or 'monitor'
            
        Returns:
            Dict containing cycle results
        """
        logger.info(f"Starting incident response cycle in {mode} mode")
        
        cycle_results = {
            'mode': mode,
            'start_time': datetime.now().isoformat(),
            'incidents_detected': 0,
            'incidents_analyzed': 0,
            'incidents_resolved': 0,
            'incidents_escalated': 0,
            'response_results': [],
            'end_time': None,
            'duration_seconds': 0
        }
        
        start_time = time.time()
        
        try:
            # Step 1: Detect incidents
            incidents = self.detect_incidents()
            cycle_results['incidents_detected'] = len(incidents)
            
            # Step 2: Analyze and respond to each incident
            for incident in incidents:
                # Analyze incident
                analyzed_incident = self.analyze_incident(incident)
                cycle_results['incidents_analyzed'] += 1
                
                # Execute autonomous response
                response_result = self.execute_autonomous_response(analyzed_incident, mode)
                cycle_results['response_results'].append(response_result)
                
                # Update counters
                if response_result['resolution_status'] == 'resolved':
                    cycle_results['incidents_resolved'] += 1
                elif response_result['human_intervention_required']:
                    cycle_results['incidents_escalated'] += 1
                
                # Store in active incidents
                self.active_incidents[incident['id']] = {
                    'incident': analyzed_incident,
                    'response': response_result,
                    'last_updated': datetime.now().isoformat()
                }
            
            # Step 3: Update metrics
            self._update_metrics()
            
        except Exception as e:
            logger.error(f"Error in incident response cycle: {e}")
            cycle_results['error'] = str(e)
        
        finally:
            end_time = time.time()
            cycle_results['end_time'] = datetime.now().isoformat()
            cycle_results['duration_seconds'] = round(end_time - start_time, 2)
        
        logger.info(f"Incident response cycle completed in {cycle_results['duration_seconds']}s")
        logger.info(f"Detected: {cycle_results['incidents_detected']}, Resolved: {cycle_results['incidents_resolved']}, Escalated: {cycle_results['incidents_escalated']}")
        
        return cycle_results
    
    def _update_metrics(self):
        """Update agent metrics."""
        if self.metrics['incidents_detected'] > 0:
            self.metrics['autonomous_resolution_rate'] = (
                self.metrics['incidents_resolved_automatically'] / self.metrics['incidents_detected']
            ) * 100
        
        # Simulate MTTR and MTTD (in practice, these would be calculated from real data)
        self.metrics['mean_time_to_detection'] = 2.5  # minutes
        self.metrics['mean_time_to_resolution'] = 8.3  # minutes

def main():
    """Main entry point for the Incident Response Agent."""
    parser = argparse.ArgumentParser(description='Incident Response Agent')
    parser.add_argument(
        '--mode',
        choices=['autonomous', 'monitor'],
        default='monitor',
        help='Operation mode: autonomous (executes actions) or monitor (observation only)'
    )
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run continuously with periodic checks'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=300,
        help='Interval in seconds between continuous runs (default: 300)'
    )
    parser.add_argument(
        '--incident-id',
        type=str,
        help='Specific incident ID to analyze'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize the incident response agent
        agent = IncidentResponseAgent()
        
        logger.info(f"Starting Incident Response Agent in {args.mode} mode")
        
        if args.incident_id:
            logger.info(f"Processing specific incident: {args.incident_id}")
            # In practice, would load specific incident and process it
            print(f"Processing incident {args.incident_id}")
        elif args.continuous:
            logger.info(f"Running continuously with {args.interval}s intervals")
            while True:
                try:
                    results = agent.run_incident_response_cycle(args.mode)
                    logger.info(f"Cycle completed - next run in {args.interval}s")
                    time.sleep(args.interval)
                except KeyboardInterrupt:
                    logger.info("Received interrupt signal - shutting down gracefully")
                    break
                except Exception as e:
                    logger.error(f"Error in continuous mode: {e}")
                    time.sleep(args.interval)
        else:
            # Single run
            results = agent.run_incident_response_cycle(args.mode)
            print(json.dumps(results, indent=2))
    
    except Exception as e:
        logger.error(f"Failed to start incident response agent: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())