"""
Mapping statistics tracker
"""
from typing import Dict, Any, List, Set, Optional
import json
import csv
from pathlib import Path
import os

class MappingTracker:
    """
    Utility for tracking and analyzing mapping statistics
    """
    
    def __init__(self):
        """
        Initialize the mapping tracker
        """
        self.stats: Dict[str, Dict[str, Any]] = {}
    
    def add_mapping_stats(self, mapper_name: str, stats: Dict[str, Any]) -> None:
        """
        Add mapping statistics for a mapper
        
        Args:
            mapper_name: Name of the mapper
            stats: Mapping statistics
        """
        self.stats[mapper_name] = stats
    
    def get_overall_stats(self) -> Dict[str, Any]:
        """
        Get overall mapping statistics
        
        Returns:
            Dict with overall statistics
        """
        total_fields = 0
        mapped_fields = 0
        unmapped_fields = 0
        mapper_coverage = {}
        
        for mapper_name, stats in self.stats.items():
            mapper_coverage[mapper_name] = stats.get('coverage_percentage', 0)
            total_fields += stats.get('total_source_fields', 0)
            mapped_fields += len(stats.get('mapped_fields', []))
            unmapped_fields += len(stats.get('unmapped_fields', []))
        
        # Calculate overall coverage
        overall_coverage = 0
        if total_fields > 0:
            overall_coverage = (mapped_fields / total_fields) * 100
        
        return {
            'total_fields': total_fields,
            'mapped_fields': mapped_fields,
            'unmapped_fields': unmapped_fields,
            'overall_coverage': overall_coverage,
            'mapper_coverage': mapper_coverage
        }
    
    def get_unmapped_fields(self) -> Dict[str, List[str]]:
        """
        Get all unmapped fields by mapper
        
        Returns:
            Dict with mapper name to list of unmapped fields
        """
        result = {}
        
        for mapper_name, stats in self.stats.items():
            result[mapper_name] = stats.get('unmapped_fields', [])
        
        return result
    
    def export_to_json(self, output_file: str) -> None:
        """
        Export statistics to JSON file
        
        Args:
            output_file: Path to output JSON file
        """
        data = {
            'mappers': self.stats,
            'overall': self.get_overall_stats()
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def export_to_csv(self, output_file: str) -> None:
        """
        Export statistics to CSV file
        
        Args:
            output_file: Path to output CSV file
        """
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(['Mapper', 'Total Fields', 'Mapped Fields', 'Unmapped Fields', 'Coverage (%)'])
            
            # Write mapper stats
            for mapper_name, stats in self.stats.items():
                writer.writerow([
                    mapper_name,
                    stats.get('total_source_fields', 0),
                    len(stats.get('mapped_fields', [])),
                    len(stats.get('unmapped_fields', [])),
                    stats.get('coverage_percentage', 0)
                ])
            
            # Write overall stats
            overall = self.get_overall_stats()
            writer.writerow([
                'OVERALL',
                overall['total_fields'],
                overall['mapped_fields'],
                overall['unmapped_fields'],
                overall['overall_coverage']
            ])
    
    def generate_report(self, output_dir: str) -> None:
        """
        Generate comprehensive mapping report
        
        Args:
            output_dir: Directory to save report files
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Export statistics to JSON and CSV
        self.export_to_json(os.path.join(output_dir, 'mapping_stats.json'))
        self.export_to_csv(os.path.join(output_dir, 'mapping_stats.csv'))
        
        # Generate HTML report
        self._generate_html_report(os.path.join(output_dir, 'mapping_report.html'))
    
    def _generate_html_report(self, output_file: str) -> None:
        """
        Generate HTML report
        
        Args:
            output_file: Path to output HTML file
        """
        overall = self.get_overall_stats()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>CDM Mapping Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2 {{ color: #333; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                .coverage-good {{ color: green; }}
                .coverage-medium {{ color: orange; }}
                .coverage-poor {{ color: red; }}
                .summary {{ margin-bottom: 20px; padding: 15px; background-color: #f0f0f0; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>CDM Mapping Coverage Report</h1>
            
            <div class="summary">
                <h2>Summary</h2>
                <p>Overall Coverage: <span class="{self._get_coverage_class(overall['overall_coverage'])}">{overall['overall_coverage']:.2f}%</span></p>
                <p>Total Fields: {overall['total_fields']}</p>
                <p>Mapped Fields: {overall['mapped_fields']}</p>
                <p>Unmapped Fields: {overall['unmapped_fields']}</p>
            </div>
            
            <h2>Mapper Coverage</h2>
            <table>
                <tr>
                    <th>Mapper</th>
                    <th>Total Fields</th>
                    <th>Mapped Fields</th>
                    <th>Unmapped Fields</th>
                    <th>Coverage (%)</th>
                </tr>
        """
        
        # Add mapper rows
        for mapper_name, stats in self.stats.items():
            coverage = stats.get('coverage_percentage', 0)
            html += f"""
                <tr>
                    <td>{mapper_name}</td>
                    <td>{stats.get('total_source_fields', 0)}</td>
                    <td>{len(stats.get('mapped_fields', []))}</td>
                    <td>{len(stats.get('unmapped_fields', []))}</td>
                    <td class="{self._get_coverage_class(coverage)}">{coverage:.2f}%</td>
                </tr>
            """
        
        # Add overall row
        html += f"""
                <tr>
                    <td><strong>OVERALL</strong></td>
                    <td><strong>{overall['total_fields']}</strong></td>
                    <td><strong>{overall['mapped_fields']}</strong></td>
                    <td><strong>{overall['unmapped_fields']}</strong></td>
                    <td class="{self._get_coverage_class(overall['overall_coverage'])}"><strong>{overall['overall_coverage']:.2f}%</strong></td>
                </tr>
            </table>
        """
        
        # Add unmapped fields details
        html += """
            <h2>Unmapped Fields by Mapper</h2>
        """
        
        for mapper_name, unmapped_fields in self.get_unmapped_fields().items():
            if unmapped_fields:
                html += f"""
                    <h3>{mapper_name}</h3>
                    <ul>
                """
                
                for field in unmapped_fields:
                    html += f"<li>{field}</li>\n"
                
                html += "</ul>\n"
            else:
                html += f"<h3>{mapper_name}</h3><p>All fields mapped successfully!</p>\n"
        
        html += """
        </body>
        </html>
        """
        
        with open(output_file, 'w') as f:
            f.write(html)
    
    def _get_coverage_class(self, coverage: float) -> str:
        """
        Get CSS class for coverage value
        
        Args:
            coverage: Coverage percentage
            
        Returns:
            CSS class name
        """
        if coverage >= 80:
            return "coverage-good"
        elif coverage >= 50:
            return "coverage-medium"
        else:
            return "coverage-poor" 