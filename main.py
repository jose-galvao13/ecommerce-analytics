"""
Script principal - Executa pipeline completo de análise
"""
import sys
from datetime import datetime
import config
from src.data_cleaning import clean_orders_data
from src.rfm_analysis import calculate_rfm
from src.cohort_analysis import cohort_retention_analysis
from src.abc_analysis import abc_analysis
from src.utils import print_section, load_data

def main():
    """Executa pipeline completo"""
    print("\n" + "="*60)
    print("  E-COMMERCE ANALYTICS PIPELINE")
    print(f"  Iniciado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    try:
        # Fase 1: Limpeza de dados
        print("\n🔄 FASE 1: Limpeza de Dados")
        df_clean = clean_orders_data()
        
        # Fase 2: Análise RFM
        print("\n🔄 FASE 2: Análise RFM")
        rfm = calculate_rfm(df_clean)
        
        # Fase 3: Análise de Cohort
        print("\n🔄 FASE 3: Análise de Cohort")
        import pandas as pd
        df_clean['order_purchase_timestamp'] = pd.to_datetime(df_clean['order_purchase_timestamp'])
        retention = cohort_retention_analysis(df_clean)
        
        # Fase 4: Análise ABC
        print("\n🔄 FASE 4: Análise ABC")
        abc = abc_analysis(df_clean)
        
        # Resumo final
        print_section("PIPELINE CONCLUÍDO COM SUCESSO")
        print(f"✅ Dados limpos salvos em: {config.DATA_PROCESSED}")
        print(f"✅ Gráficos salvos em: {config.OUTPUTS_PLOTS}")
        print(f"✅ Relatórios salvos em: {config.OUTPUTS_REPORTS}")
        print(f"✅ Tempo de execução: {datetime.now()}")
        
        print("\n📊 Próximos passos:")
        print("   1. Importar dados para SQL (ver pasta data/sql/)")
        print("   2. Abrir dashboard no Power BI")
        print("   3. Revisar insights em outputs/reports/")
        
    except Exception as e:
        print(f"\n❌ ERRO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()