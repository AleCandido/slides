import styles from "./presentation.module.css";

export default function Presentation({ children, href }) {
  return (
    <a className={styles.card} href={href}>
      {children}
    </a>
  );
}
