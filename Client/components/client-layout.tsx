"use client";

import { ThemeProvider } from "@/components/theme-provider";
import Header from "@/components/ui/header";
import Footer from "@/components/ui/footer";
import { Toaster } from "sonner";

export default function ClientLayout({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider>
      <Header />
      <main>{children}</main>
      <Footer />
      <Toaster position="top-right" />
    </ThemeProvider>
  );
}